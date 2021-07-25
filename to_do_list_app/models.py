from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class TodolistModel(models.Model):
    task = models.TextField(max_length = 140)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
