from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('list/', ExercisesListView.as_view(), name='exercises'),
    path('<slug:task_name>/', ExercisesDetailView.as_view(), name='exercise-detail'),
]