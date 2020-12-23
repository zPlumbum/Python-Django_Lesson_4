from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.TextField(verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    image = models.TextField(verbose_name='Картинка')
    release_date = models.DateField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField()

    def __str__(self):
        return f"Модель: {self.name}, цена: {self.price}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
