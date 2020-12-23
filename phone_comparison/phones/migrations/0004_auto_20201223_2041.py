# Generated by Django 3.1.4 on 2020-12-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20201223_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='double_camera',
            field=models.TextField(blank=True, null=True, verbose_name='Двойная камера'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='manufacturer',
            field=models.TextField(blank=True, choices=[('CN', 'Китай'), ('VN', 'Вьетнам'), ('RU', 'Россия')], null=True),
        ),
    ]
