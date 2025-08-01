# Generated by Django 5.2.4 on 2025-07-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('profession', models.CharField(default='Student', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_solved_problem', models.CharField(default='0', max_length=50)),
                ('languages', models.CharField(max_length=500)),
                ('dbms', models.CharField(max_length=500)),
                ('softwares', models.CharField(max_length=500)),
                ('others', models.CharField(max_length=1000)),
                ('projects', models.JSONField(default=list)),
            ],
        ),
    ]
