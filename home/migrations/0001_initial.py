# Generated by Django 5.0.2 on 2024-02-14 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блока сервисов')),
                ('description', models.TextField(verbose_name='Описание блока сервисов')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('description', models.TextField(max_length=800, unique=True)),
                ('icon', models.CharField(max_length=100)),
                ('is_visible', models.BooleanField(default=True)),
                ('service_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='home.serviceblock', verbose_name='Блок сервисов')),
            ],
            options={
                'verbose_name_plural': 'Services',
                'ordering': ('position',),
            },
        ),
    ]
