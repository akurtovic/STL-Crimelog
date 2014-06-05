from django.db import models

class Story(models.Model):
    headline = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    source = models.CharField(max_length=50)
    added = models.DateTimeField()