# Generated by Django 3.1.4 on 2020-12-22 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('image', models.FilePathField(verbose_name='Картинка')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
                ('lte_exists', models.BooleanField(verbose_name='Наличие LTE')),
                ('slug', models.SlugField(verbose_name=models.TextField(verbose_name='Название'))),
            ],
        ),
    ]