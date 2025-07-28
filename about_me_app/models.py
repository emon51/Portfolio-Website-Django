from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    age = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 15)
    profession = models.CharField(max_length = 500, default = 'Student')


    def __str__(self):
        return self.name
    


class Skills(models.Model):
    number_of_solved_problem = models.CharField(max_length = 50, default = '0')
    languages = models.CharField(max_length = 500)
    dbms = models.CharField(max_length = 500)
    softwares = models.CharField(max_length = 500)
    others = models.CharField(max_length = 1000)
    projects = models.JSONField(default = list) #["project_name", "source_code_url", "live_url"]

   
    