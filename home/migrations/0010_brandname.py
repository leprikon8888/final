# Generated by Django 5.0.2 on 2024-02-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_shapka_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="ім'я бренду")),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
