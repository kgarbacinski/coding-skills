from django.db import models
from django.utils import timezone

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.TextField(blank=False, default='')
    task_content = models.TextField(blank=False, default='')
    task_created = models.DateTimeField(default=timezone.now) 

    def __str__(self) -> str:
        return f'{self.task_id=}, {self.task_name=}, {self.task_content=}, {self.task_created=}'


class Tests(models.Model):
    test_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey('Tasks', on_delete=models.SET_NULL, null=True)
    test_input = models.TextField(blank=False)
    test_output = models.TextField(blank=False)
    test_language = models.TextField(blank=False)
    test_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str: 
        return f'{self.test_id=}, {self.task_id=}, {self.test_input=}, {self.test_output=}, {self.test_language=}'