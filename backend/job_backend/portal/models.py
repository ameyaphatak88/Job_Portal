from django.db import models

class Job(models.Model):
    company = models.CharField(max_length = 20)
