from django.db import models
from django import forms


schoices = [('C++', 'C++'),
            ('Python', 'Python'),]

class Job(models.Model):
    company = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    primary_skill = forms.RadioSelect(choices = schoices)
    min_work_experience = forms.IntegerField(label = 'min_work_experience')