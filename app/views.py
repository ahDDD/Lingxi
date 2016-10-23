from django.shortcuts import render

# Create your views here.


def base(request):
    context = {}
    return render(request, 'base.html', context)


def login(request):
    return render(request, 'login.html')