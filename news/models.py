from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from taggit.managers import TaggableManager

from comments.models import Comment


def content_file_name(instance, filename):
    return f'images/{instance.__class__.__name__}/{filename}'


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='Слаг', db_index=True, unique=True, blank=True)
    description = models.CharField(max_length=250, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, verbose_name='Слаг', unique=True, blank=True)
    content = models.TextField(verbose_name='Содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='post_author')
    image = models.ImageField(upload_to=content_file_name, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category',
                                 verbose_name='Категория')
    comments = GenericRelation(Comment)
    tags = TaggableManager(verbose_name='Теги', )
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title} - {self.created}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="75" height="75">')  # блок кода,который выводит картинку

    get_image.short_description = 'Превью'  # название

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
