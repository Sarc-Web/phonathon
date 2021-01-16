from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUser(AbstractUser):
    is_staff = models.BooleanField(default = False)
    is_supervisor = models.BooleanField(default = False)

    def __str__(self):
        return (self.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Student(models.Model):
    ldap = models.CharField(max_length=9)
    department = models.CharField(max_length=100)
    
    year = models.IntegerField()
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student")
    phone = models.IntegerField()
    sheets = models.ManyToManyField('Users.Sheet', related_name="allocated_sheets", blank=True)

    def __str__(self):
        return self.ldap

class Sheet(models.Model):
    batch = models.IntegerField()
    year = models.IntegerField()
    url = models.TextField(primary_key = False)

    def __str__(self):
        return self.url

class worksheet(models.Model):
    
    worksh = models.ForeignKey(Sheet,on_delete = models.CASCADE)




class Alum_Detail(models.Model):
    
    Alum = models.ForeignKey(worksheet,on_delete = models.CASCADE)
    name = models.CharField(max_length=55)
    contactno1 = models.IntegerField()
    contactno2 = models.IntegerField(blank=True, null=True)
    contactno3 = models.IntegerField(blank=True, null=True)
    contactno4 = models.IntegerField(blank=True, null=True)
    contactno5 = models.IntegerField(blank=True, null=True)
    email1 = models.EmailField(max_length=60)
    email2 = models.EmailField(max_length=60,blank=True, null=True)
    email3 = models.EmailField(max_length=60,blank=True, null=True)
    email4 = models.EmailField(max_length=60,blank=True, null=True)
    email5 = models.EmailField(max_length=60,blank=True, null=True)
    ilp = models.CharField(max_length=60,blank=True, null=True)
    core_talks = models.CharField(max_length=60,blank=True, null=True)
    MI_GD = models.CharField(max_length=60,blank=True, null=True)
    Sarc_Blog = models.CharField(max_length=60,blank=True, null=True)
    newsletter = models.CharField(max_length=60,blank=True, null=True)
    newsletter_feedback =models.CharField(max_length=600,blank=True, null=True)
    permanent_address = models.CharField(max_length=1000,blank=True, null=True)
    temporary_address = models.CharField(max_length=1000,blank=True, null=True)
    class_of = models.IntegerField(blank=True, null=True)
    degree = models.CharField(max_length=100,blank=True, null=True)    
    hostelno = models.IntegerField(blank=True, null=True)
    dept = models.CharField(max_length=100,blank=True, null=True)     
    Organization_name = models.CharField(max_length=200,blank=True, null=True)
    designation = models.CharField(max_length=200,blank=True, null=True)
    working_place = models.CharField(max_length=200,blank=True, null=True)
    remark = models.CharField(max_length=600,blank=True, null=True)
    status = models.CharField(max_length=45,blank=True, null=True)
    extra1 = models.CharField(max_length=60,blank=True, null=True)
    extra2 = models.CharField(max_length=60,blank=True, null=True)
    extra3 = models.CharField(max_length=60,blank=True, null=True)
    extra4 = models.CharField(max_length=60,blank=True, null=True)
    extra5 = models.CharField(max_length=60,blank=True, null=True)
    extra6 = models.CharField(max_length=60,blank=True, null=True)