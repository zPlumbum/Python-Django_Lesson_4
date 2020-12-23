from django.db import models


class CountryChoices(models.TextChoices):
    CHINA = 'CN', 'Китай'
    VIETNAM = 'VN', 'Вьетнам'
    RUSSIA = 'RU', 'Россия'


class Phone(models.Model):
    name = models.TextField(verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    SIM_count = models.IntegerField(verbose_name='Количество симок')
    OS_type = models.TextField(verbose_name='ОС')
    resolution = models.TextField(verbose_name='Разрешение')
    manufacturer = models.TextField(choices=CountryChoices.choices, null=True, blank=True)
    brand = models.ForeignKey('Brand',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True
                              )
    double_camera = models.TextField(verbose_name='Двойная камера', null=True, blank=True)
    headphones_port = models.TextField(verbose_name='Разъем для наушников')

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    name = models.TextField(verbose_name='Название')
    features = models.TextField(verbose_name='Особенности', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
