from django.shortcuts import render
from app.models import Question, Answer, UserProfile
# Create your views here.


def base(request):
    context = {}
    questions = Question.objects.all().order_by('-create_time')
    user_profile = UserProfile.objects.get(belong_to=request.user)
    context['questions'] = questions[:5]
    context['new_question'] = user_profile.user_question.all().order_by('-create_time').first()
    context['new_answer'] = user_profile.user_answer.all().order_by().first()
    user_profile = UserProfile.objects.all()
    context['user_profile'] = user_profile
    return render(request, 'base.html', context)