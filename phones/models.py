from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, verbose_name="Модель")
    slug = models.SlugField(max_length=150, verbose_name="Slug")
    image = models.URLField(verbose_name="Фото")
    price = models.IntegerField(verbose_name="Цена")
    release_data = models.DateField(verbose_name="Реализ")
    lte_exist = models.BooleanField(verbose_name="LTE")
