# Generated by Django 3.2.6 on 2021-08-26 21:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tasks",
            fields=[
                ("task_id", models.AutoField(primary_key=True, serialize=False)),
                ("task_name", models.TextField(default="")),
                ("task_content", models.TextField(default="")),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Tests",
            fields=[
                ("test_id", models.AutoField(primary_key=True, serialize=False)),
                ("test_input", models.TextField()),
                ("test_output", models.TextField()),
                ("language", models.TextField()),
                (
                    "task_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="exercises.tasks",
                    ),
                ),
            ],
        ),
    ]
