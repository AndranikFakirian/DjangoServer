from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=5000)
    password = models.CharField(max_length=10)
    state = models.CharField(max_length=30)