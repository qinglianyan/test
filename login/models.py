from django.db import models

# Creat user models
class User(models.Model):
    Username=models.CharField(max_length=32,primary_key=true)
    Password=models.CharField(max_length=32)
    #sex=models.BooleanField(max_length=1, choices=((0,'男'),(1,'女')))
    telephone=models.Carfield(max_length=50,blank=True),
    email=models.EmailField(max_length=254,unique=True, blank=False)
    mod_data=models.DateTimeField(auto_now=True)