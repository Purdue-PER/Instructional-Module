from django.db import models

# Create your models here.
class llm_data(models.Model):
    user = models.CharField(max_length=25)
    message = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000) 
