from django.shortcuts import render
from app.models import Question, Answer, UserProfile
# Create your views here.


def base(request):
    context = {}
    questions = Question.objects.all().order_by('-create_time')
    context['questions'] = questions
    user_profile = UserProfile.objects.all()
    context['user_profile'] = user_profile
    return render(request, 'base.html', context)