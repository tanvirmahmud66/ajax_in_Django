from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class NameDB(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name
    


