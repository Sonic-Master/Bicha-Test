from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class signup(models.Model):
    givenname       =   models.CharField(max_length=200)
    surename        =   models.CharField(max_length=200)
    username        =   models.ForeignKey(User,on_delete=models.CASCADE)