# Generated by Django 5.0.3 on 2025-04-19 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_me_app', '0007_about_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='profile_image',
        ),
    ]
