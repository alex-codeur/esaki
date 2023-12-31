# Generated by Django 4.2.2 on 2023-06-17 08:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('publish', models.DateTimeField(default=datetime.datetime(2023, 6, 17, 8, 12, 34, 571145, tzinfo=datetime.timezone.utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
