# Generated by Django 4.2 on 2023-05-07 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_user_puid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]