# Generated by Django 3.2.7 on 2021-09-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
