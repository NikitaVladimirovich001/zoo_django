from django.db import models


class KommentModel(models.Model):
    name = models.CharField(max_length=32)
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)


class Animals(models.Model):
    img = models.ImageField(upload_to = 'img' )
    name = models.CharField(max_length=50, verbose_name='Кличка')
    age = models.CharField(max_length=10,  verbose_name='Возраст')
    description = models.TextField(verbose_name='Описание')




