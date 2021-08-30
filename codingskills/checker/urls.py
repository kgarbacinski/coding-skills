from django.urls import path
from .views import GetExercise

urlpatterns = [
    path('post/', GetExercise.as_view(), name='getExercise'),
]