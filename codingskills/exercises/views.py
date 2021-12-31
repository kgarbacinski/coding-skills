from django.shortcuts import render
from .models import Tasks, Tests
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def home(request):
    """
    'Home' page view. Uses home.html template for render and reads the data from DB.
    """
    return render(request, 'exercises/home.html', 
    {
        'title': 'Home',
        'text': 'Welcome to Coding Exercises!',
        'tasks': Tasks.objects.all()
        })


class ExercisesDetailView(DetailView):
    model = Tasks
    template_name = 'exercises/exercise_view.html'
    slug_url_kwarg = 'task_name'
    slug_field = 'task_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = Tests.objects.filter(task_id = self.object)
        return context
       