# Generated by Django 5.0.2 on 2024-02-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_contactblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactblock',
            name='photo',
            field=models.ImageField(blank=True, upload_to='bg_contacts/'),
        ),
    ]
