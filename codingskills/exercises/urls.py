from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('exercises/', ExercisesListView.as_view(), name='exercises'),
    path('exercises/<slug:task_name>/', ExercisesDetailView.as_view(), name='exercise-detail'),
]