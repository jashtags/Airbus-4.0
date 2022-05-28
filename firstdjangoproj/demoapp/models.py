from django.db import models

# Create your models here.
class Todo (models.Model):
    Task= models.CharField(max_length= 20)
    Description = models.CharField(max_length= 20)