from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=300,unique=True)


    def __str__(self):
        return self.top_name


class Webpage(models.Model):
        topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
        name=models.CharField(max_length=300,unique=True)
        URL=models.URLField(unique=True)


        def __str__(self):
            return self.name


class AccessRecords(models.Model):
    name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date=models.DateField()


    def __str__(self):
        return str(self.date)



'''class User(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    phone = models.CharField( max_length=17, blank=True) # validators should be a list


    def __str__(self):
        return self.name + ', ' + self.last_name + ': ' + self.email + ': ' + self.phone'''


class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    #additional
    portfolio_site=models.URLField(blank=True)

    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
