# Generated by Django 5.0.2 on 2024-02-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, upload_to='client/')),
            ],
        ),
    ]
