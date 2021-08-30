from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exercises.urls')),
    path('post/', include('checker.urls'))
]
