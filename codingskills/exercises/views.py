from django.shortcuts import render
from .models import Tasks, Tests
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def home(request):
    return render(request, 'exercises/home.html', 
    {
        'title': 'Home',
        'text': 'Welcome to Coding Exercises!'
        })

def about(request): 
    return render(request, 'exercises/about.html', {'text': 'About'})

def exercises(request):
       return render(request, 'exercises/exercises.html', 
    {
        'title': 'Exercises',
        'exercises': Tasks.objects.all()
        })

class ExercisesListView(ListView):
    model = Tasks
    template_name = 'exercises/exercises.html'
    context_object_name = 'exercises'
    ordering = ['-task_created']

class ExercisesDetailView(DetailView):
    model = Tasks
    template_name = 'exercises/exercise_view.html'