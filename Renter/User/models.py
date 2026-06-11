from django.db import models
from Guest.models import *
from Renter.models import *
# Create your models here.
class tbl_Complaint(models.Model):
    Complaint_subject=models.CharField(max_length=30)
    Complaint_complaint=models.CharField(max_length=30)
    User_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    complaint_status=models.IntegerField(default=0)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=40)
    complaint_replydate=models.DateField(null=True)
    
class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=30)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_Request(models.Model):
    Request_status=models.IntegerField(default=0)
    Request_date=models.DateField(auto_now_add=True)
    Request_fordate=models.DateField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(tbl_Vehicle,on_delete=models.CASCADE)
    Request_startKm=models.CharField(max_length=30,null=True)
    Request_endKm=models.CharField(max_length=30,null=True)
    Request_amount=models.CharField(max_length=30)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    vehicle=models.ForeignKey(tbl_Vehicle,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)