from django.db import models

# Create your models here.
class clicks(models.Model):
    user = models.CharField(max_length=25)
    mouseX = models.CharField(max_length=25,blank=True)
    mouseY = models.CharField(max_length=25,blank=True)
    time_stamp = models.CharField(max_length=100,blank=True)
    event = models.CharField(max_length=200,blank=True)

