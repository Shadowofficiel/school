# Generated by Django 2.2.12 on 2024-12-26 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200420_2333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={},
        ),
        migrations.AddField(
            model_name='quiz',
            name='nombre_tentatives',
            field=models.IntegerField(default=1),
        ),
    ]