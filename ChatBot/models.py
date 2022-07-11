from datetime import datetime
from pyexpat import model
from django.db import models

class Chat(models.Model):
    message = models.CharField(max_length=1000000)
    response = models.CharField(max_length=1000000)
    time = models.DateTimeField(default=datetime.now,blank=True)