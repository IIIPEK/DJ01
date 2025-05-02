from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    title = models.CharField('Title', max_length=200)
    description = models.CharField('Description', max_length=200)
    text = models.TextField('Text')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"