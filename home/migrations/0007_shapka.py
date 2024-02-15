# Generated by Django 5.0.2 on 2024-02-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shapka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
            ],
        ),
    ]
