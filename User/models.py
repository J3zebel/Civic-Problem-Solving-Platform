from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_complaint(models.Model):
    complaint_content=models.CharField(max_length=200)
    complaint_photo=models.URLField()
    complaint_response=models.CharField(max_length=200)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    kseb=models.ForeignKey(tbl_kseb,on_delete=models.CASCADE,null=True)
    mvd=models.ForeignKey(tbl_mvd,on_delete=models.CASCADE,null=True)
    pwd=models.ForeignKey(tbl_pwd,on_delete=models.CASCADE,null=True)
    muncipality=models.ForeignKey(tbl_muncipality,on_delete=models.CASCADE,null=True)
    complaint_status=models.IntegerField(default=0)
    complaint_date=models.DateField(auto_now_add=True)


class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=200)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    feedback_date=models.DateField(auto_now_add=True)

class tbl_like(models.Model):
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    complaint=models.ForeignKey(tbl_complaint,on_delete=models.CASCADE)

class tbl_request(models.Model):
    request_title=models.CharField(max_length=30)
    request_content=models.CharField(max_length=200)
    request_response=models.CharField(max_length=200)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    muncipality=models.ForeignKey(tbl_muncipality,on_delete=models.CASCADE,null=True)
    kseb=models.ForeignKey(tbl_kseb,on_delete=models.CASCADE,null=True)
    mvd=models.ForeignKey(tbl_mvd,on_delete=models.CASCADE,null=True)
    request_status=models.IntegerField(default=0)
    request_date=models.DateField(auto_now_add=True)