from django.db import models
# from django.conf import settings
# from django.utils.text import slugify
# from django.db.models.signals import pre_save
# from django.urls import reverse

# Create your models here.

#we write schemas of database in modsl
class Article(models.Model):
    title =models.CharField(max_length =100, unique=True)
    image =models.ImageField(upload_to='article/',default='default.jpg',blank=True,null =True)
    date =models.DateTimeField()
    content =models.TextField()
    draft = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Hero(models.Model):
    image = models.ImageField(upload_to='hero/',default='default.jpg')
    caption = models.CharField(max_length=250)
    sub_heading = models.CharField(max_length =100)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.caption


class Contact(models.Model):
    full_name = models.CharField("Full Name", max_length = 100)
    email = models.EmailField("Enter Email", max_length=250)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20) #no need to give the max_length in the integer and Text field
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.full_name
