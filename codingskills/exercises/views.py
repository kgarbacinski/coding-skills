from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'exercises/home.html', {'text': 'Home'})

def about(request): 
    return render(request, 'exercises/about.html', {'text': 'About'})

def exercises(request):
    return HttpResponse('Exercises leave here')