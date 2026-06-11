from django.db import models
from Admin.models import *

# Create your models here.
class tbl_user(models.Model):
    User_name=models.CharField(max_length=30)
    User_Email=models.CharField(max_length=30)
    User_contact=models.CharField(max_length=30)
    User_address=models.CharField(max_length=80)
    User_Password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    User_photo=models.FileField(upload_to='Assets/File/User')


# Create your models here.
class tbl_Renter(models.Model):
    Renter_name=models.CharField(max_length=30)
    Renter_Email=models.CharField(max_length=30)
    Renter_contact=models.CharField(max_length=30)
    Renter_address=models.CharField(max_length=80)
    Renter_Password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    Renter_photo=models.FileField(upload_to='Assets/File/Renter')
    Renter_proof=models.FileField(upload_to='Assets/File/Renter')
    Renter_status = models.IntegerField(default=0)
    
