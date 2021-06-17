from django import forms
from django.db import models
class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    phone=models.IntegerField()
    pic=models.ImageField(upload_to='images')
    st_id=models.IntegerField(blank=True,null=True)


class usercreation(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(unique=True)
    user_pic = models.ImageField(upload_to='user/images')
    user_password = models.CharField(max_length=100)


class login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)