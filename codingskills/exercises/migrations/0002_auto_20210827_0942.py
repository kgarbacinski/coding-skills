# Generated by Django 3.2.6 on 2021-08-27 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tasks",
            old_name="created",
            new_name="task_created",
        ),
        migrations.RenameField(
            model_name="tests",
            old_name="language",
            new_name="test_language",
        ),
        migrations.AddField(
            model_name="tests",
            name="test_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
