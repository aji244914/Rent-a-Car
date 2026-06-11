from django.db import models
from Admin.models import *
from Guest.models import *


class tbl_Vehicle(models.Model):
    Vehicle_name=models.CharField(max_length=30)
    Vehicle_image=models.FileField(upload_to='Assets/File/Vehicle/')
    vehicletype=models.ForeignKey(tbl_vehicletype,on_delete=models.CASCADE)
    Vehicle_minkm=models.CharField(max_length=30)
    Vehicle_minrate=models.CharField(max_length=30)
    Vehicle_kmrate=models.CharField(max_length=80)
    renter=models.ForeignKey(tbl_Renter,on_delete=models.CASCADE)

class tbl_VehicleGallery(models.Model):
    Vehicle_photo=models.FileField(upload_to='Assets/File/Vehiclegallery/')
    vehicle=models.ForeignKey(tbl_Vehicle,on_delete=models.CASCADE)
