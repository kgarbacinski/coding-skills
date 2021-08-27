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
    return render(request, 'exercises/about.html', {'title': 'About'})

class ExercisesListView(ListView):
    model = Tasks
    template_name = 'exercises/exercises.html'
    context_object_name = 'exercises'
    ordering = ['-task_created']


class ExercisesDetailView(DetailView):
    model = Tasks
    template_name = 'exercises/exercise_view.html'
    slug_url_kwarg = 'task_name'
    slug_field = 'task_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = Tests.objects.filter(task_id = self.object)
        return context
       