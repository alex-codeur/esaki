# Generated by Django 4.2.2 on 2023-06-25 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 25, 9, 20, 18, 517060, tzinfo=datetime.timezone.utc)),
        ),
    ]