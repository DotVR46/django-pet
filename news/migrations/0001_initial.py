# Generated by Django 3.2.7 on 2021-09-05 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Слаг')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Слаг')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('image', models.ImageField(upload_to=news.models.content_file_name)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='news.category')),
            ],
        ),
    ]
