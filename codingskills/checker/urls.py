from django.urls import path
from .views import HandleFrontendData

urlpatterns = [
    path('post/', HandleFrontendData.as_view(), name='frontend-data'),
]