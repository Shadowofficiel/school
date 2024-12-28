# Generated by Django 2.2.12 on 2024-12-28 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_studentanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswer',
            name='quiz_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_answers', to='quiz.QuizResult'),
        ),
    ]
