from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'todopages/home.html', {})

def login(request):
    return render(request, 'todopages/login.html', {})

def register(request):
    return render(request, 'todopages/register.html', {})