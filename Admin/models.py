from django.db import models
from Admin.models import *

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)
class tbl_Admin(models.Model):
    Admin_name=models.CharField(max_length=30)
    Admin_Email=models.CharField(max_length=30)
    Admin_Password=models.CharField(max_length=30)
class tbl_Category(models.Model):
    Category_name=models.CharField(max_length=30)
class tbl_place(models.Model):
    place_name=models.CharField(max_length=30)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_SubCategory(models.Model):
    Subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_Category,on_delete=models.CASCADE)
class tbl_vehicletype(models.Model):
    vehicletype_name=models.CharField(max_length=30)
