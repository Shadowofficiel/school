# Generated by Django 2.2.12 on 2024-12-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_privatemessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
