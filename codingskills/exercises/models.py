from django.db import models
from django.utils import timezone


class Tasks(models.Model):
    """
    DB model to store tasks related data.
    Fields:
        task_id (primary_key): int.
        task_name: string. Sample value - 'palindrome'
        task_content: string. Sample value - 'Check if given string is a palindrome. Function should return boolean value <True> or <False>.'
        task_created: timestamp.

    One task can contain multiple tests (1 per language).
    """

    task_id = models.AutoField(primary_key=True)
    task_name = models.TextField(blank=False, default="")
    task_content = models.TextField(blank=False, default="")
    task_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        """
        Overloaded in-built method to stringify DB content (vs printing object representation).
        """
        return f"{self.task_id=}, {self.task_name=}, {self.task_content=}, {self.task_created=}"


class Tests(models.Model):
    """
    DB model to store language-specific exercise data. Joined with Tasks on Tasks.task_id = Tests.task_id
    Fields:
        test_id (primary_key): int.
        task_id: int. Linked task entity where task content is stored.
        test_input: string. Predefined input to be used in exercise.
        test_output: string. Predefined output to be used in exercise. Input and output will be asserted during the remote execution.
        test_language: string. Language in which exercise should be solved (Python, Node, Java).
        test_created: timestamp.
    """

    test_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey("Tasks", on_delete=models.SET_NULL, null=True)
    test_input = models.TextField(blank=False)
    test_output = models.TextField(blank=False)
    test_language = models.TextField(blank=False)
    test_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        """
        Overloaded in-built method to stringify DB content (vs printing object representation).
        """
        return f"{self.test_id=}, {self.task_id=}, {self.test_input=}, {self.test_output=}, {self.test_language=}"
