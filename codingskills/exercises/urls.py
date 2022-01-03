from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.ExerciseHomeView.as_view(), name='home'),
    path('<slug:task_name>/', ExercisesDetailView.as_view(), name='exercise-detail'),
]