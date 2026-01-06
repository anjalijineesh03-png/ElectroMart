from django.db import models

# Create your models here.

class User_RegistrationDB(models.Model):
    User_name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirm_Password = models.CharField(max_length=100, null=True, blank=True)
class ContactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    MobileNo = models.IntegerField(null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.TextField(null=True, blank=True)
