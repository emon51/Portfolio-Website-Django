# Generated by Django 5.0.3 on 2025-04-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me_app', '0005_alter_about_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='projects',
            field=models.JSONField(default=list),
        ),
    ]
