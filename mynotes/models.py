from pickle import TRUE
from django.contrib.auth.models import AbstractUser,User
from django.db import models
import datetime

#username, email, password, 
class User(AbstractUser):
    pass
    def __str__(self):
        return f"{self.id}--{self.username}"
# Create your models here.
class Notes(models.Model):
    content=models.TextField(max_length=10000)
    Title=models.CharField(max_length=64)
    owner= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Wishlist= models.BooleanField(default = False)
    def __str__(self):
        return f"{self.id}-{self.Title}- {self.owner}"

