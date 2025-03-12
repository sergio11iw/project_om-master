# Generated by Django 5.1.6 on 2025-02-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('sitze', models.TextField(blank=True, null=True, verbose_name='Размеры')),
                ('color1', models.TextField(max_length=100)),
                ('color2', models.TextField(max_length=100)),
                ('color3', models.TextField(max_length=100)),
                ('descr', models.TextField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Изделия',
                'verbose_name_plural': 'Изделия',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('tel', models.PositiveIntegerField(verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]
