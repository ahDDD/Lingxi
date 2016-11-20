from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from app.models import Question, Answer, UserProfile, Comment
from app.forms import AnswerForm, CommentForm


def base(request):
    context = {}
    questions = Question.objects.all().order_by('-create_time')
    context['questions'] = questions
    user_profile = UserProfile.objects.all()
    context['user_profile'] = user_profile
    return render(request, 'base.html', context)


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
