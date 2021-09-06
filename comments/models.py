from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=300, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, db_index=True,
                               on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.content_type} - {self.content_object.id} | {self.content_object}'

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
