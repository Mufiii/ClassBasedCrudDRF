from django.db import models

# Create your models here.

class Football(models.Model):
    team = models.CharField(max_length=150)
    player = models.CharField(max_length=150)
    jersey_no = models.IntegerField()