from django.db import models
from django import forms


schoices = [('C++', 'C++'),
            ('Python', 'Python'),]

class Job(models.Model):
    company = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    min_work_experience = models.IntegerField(default = 0)
    primary_skill = models.CharField(max_length = 20, default = "C++")
