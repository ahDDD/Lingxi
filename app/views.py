#coding:utf-8
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from app.models import Question, Answer, UserProfile, Comment
from app.forms import AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger
import functools
# Create your views here.


def base(request):
    context = {}
    # 以下内容务必传出
    # -----------------
    hot_questions = Question.objects.all().order_by('-create_time')
    # 总问题数
    context['count_questions'] = len(hot_questions)
    # 总人数
    context['count_users'] = len(UserProfile.objects.all())
    # 右侧热点top5
    context['questions'] = hot_questions[:5]
    if request.user.is_anonymous:
        pass
    else:
        user_profile = UserProfile.objects.get(belong_to=request.user)
        # 左侧你提问
        context['new_question'] = user_profile.user_question.all().order_by('-create_time').first()
        # 左侧你回答
        context['new_answer'] = user_profile.user_answer.all().order_by().first()
    # -----------------
    return context

def index(request, limit=15):
    context = {}
    if not limit:
        limit = 15

    hot_questions = Question.objects.all().order_by('-create_time')
    # 总问题数
    context['count_questions'] = len(hot_questions)
    # 总人数
    context['count_users'] = len(UserProfile.objects.all())
    # 右侧热点top5
    context['questions'] = hot_questions[:5]
    if request.user.is_anonymous:
        pass
    else:
        user_profile = UserProfile.objects.get(belong_to=request.user)
        # 左侧你提问
        context['new_question'] = user_profile.user_question.all().order_by('-create_time').first()
        # 左侧你回答
        context['new_answer'] = user_profile.user_answer.all().order_by().first()


    oreder_by = request.GET.get('order_by')
    print(oreder_by)
    if oreder_by == "time":
        ques_list = Question.objects.all().order_by('-create_time')
    elif oreder_by == "votes":
        ques_list = Question.objects.all().order_by('-votes')
    elif oreder_by == "unanswer":
        ques_list = Question.objects.filter(question_answer=None)
    else:
        ques_list = Question.objects.all().order_by('-create_time')

    context['questions'] = hot_questions
    user_profile = UserProfile.objects.all()
    context['user_profile'] = user_profile
    paginator = Paginator(ques_list, limit)  # 实例化一个分页对象
    page = request.GET.get('page')
    try:
        ques = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        ques = paginator.page(1)  # 取第一页的记录
        page = 1
    except EmptyPage:  # 如果页码太大，没有相应的记录
        ques = paginator.page(paginator.num_pages)  # 取最后一页的记录
        page = paginator.num_pages


    page_list = []
    indexperpage = 5
    if page is not None:
        start_page = int(page) - (int(page)-1) % indexperpage
    else:
        start_page = 1

    for i in range(5):
        if i+start_page > paginator.num_pages:
            break
        page_list.append(i+start_page)

    context['page_list'] = page_list
    context['ques'] = ques
    return render(request, 'index.html', context)

@login_required
def profile(request):
    context = base(request)
    user_proflie = UserProfile.objects.get(belong_to=request.user)
    questions = Question.objects.filter(questioner=user_proflie).order_by("-update_time")
    context['ques'] = questions
    context['questions_count'] = len(questions)
    return render(request, 'profile.html', context)


def details(request, **kwargs):
    context = {}
    answer_tag = request.GET.get('answer_tag')
    question_id = kwargs['question_id']
    question = Question.objects.get(id=question_id)
    best_answers = Answer.objects.filter(best_answer=True,
                                         belong_to_question=question)
    answers = Answer.objects.filter(best_answer=False,
                                    belong_to_question=question)
    if answer_tag == 'votes':
        answers = answers.order_by('-votes')
    elif answer_tag == 'oldest':
        answers = answers.order_by('create_time')
    if best_answers:
        context['best_answers'] = best_answers
    if request.method == 'POST' and 'answer' in request.POST.keys():
        context['form'] = deal_with_answer(request, question)
    else:
        context['form'] = AnswerForm
    context['question'] = question
    context['answers'] = answers
    return render(request, 'details.html', context)


def deal_with_answer(request, question):
    form = AnswerForm(request.POST)
    print('arrive deal_with_answer')
    if form.is_valid():
        answer = form.cleaned_data['answer']
        c = Answer(answerer=request.user.profile, belong_to_question=question)
        c.content = answer
        c.save()
        return AnswerForm
    else:
        return form


def deal_with_comment(request, **kwargs):
    question_id = kwargs['question_id']
    answer_id = kwargs['answer_id']
    answer = Answer.objects.get(id=answer_id)
    comment = request.POST.get('comment')
    c = Comment(user=request.user, belong_to_answer=answer)
    c.comment = comment
    c.save()
    return details(request, question_id=question_id)
