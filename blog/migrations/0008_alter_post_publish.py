# Generated by Django 4.2.2 on 2023-06-21 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_comment_email_remove_comment_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 21, 7, 58, 53, 561392, tzinfo=datetime.timezone.utc)),
        ),
    ]
