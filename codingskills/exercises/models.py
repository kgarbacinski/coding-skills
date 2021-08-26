from django.db import models
from django.utils import timezone

class Exercise(models.Model):
    exercise = models.AutoField(primary_key=True)
    exercise_content = models.TextField(blank=False)
    created = models.DateTimeField(default=timezone.now)


class Tests(models.Model):
    test_id = models.AutoField(primary_key=True)
    exercise = models.ForeignKey('Exercise', on_delete=models.SET_NULL, null=True)
    test_input = models.TextField(blank=False)
    test_result = models.TextField(blank=False)
    language = models.TextField(blank=False)