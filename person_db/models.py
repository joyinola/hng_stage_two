from django.db import models





# Create your models here.


class Physique(models.Model):
    height=models.CharField(max_length=255,blank=True,null=True)
    weight=models.CharField(max_length=255,blank=True,null=True)
    complexion=models.CharField(max_length=255,blank=True,null=True)

class Address(models.Model):
    state=models.CharField(max_length=255,blank=True,null=True)
    area=models.CharField(max_length=255,blank=True,null=True)
    house_no=models.CharField(max_length=255,blank=True,null=True)

class Person(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True,blank=True,null=True)
    physique=models.OneToOneField(Physique,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.ForeignKey(Address,on_delete=models.SET_NULL,blank=True,null=True)

    
