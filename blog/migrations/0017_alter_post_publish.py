# Generated by Django 4.2.2 on 2023-06-22 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 22, 18, 7, 41, 437104, tzinfo=datetime.timezone.utc)),
        ),
    ]