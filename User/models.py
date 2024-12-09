from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_complaint(models.Model):
    complaint_content=models.CharField(max_length=200)
    complaint_photo=models.URLField()
    complaint_title=models.CharField(max_length=30)
    complaint_response=models.CharField(max_length=200)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    kseb=models.ForeignKey(tbl_kseb,on_delete=models.CASCADE,null=True)
    mvd=models.ForeignKey(tbl_mvd,on_delete=models.CASCADE,null=True)
    pwd=models.ForeignKey(tbl_pwd,on_delete=models.CASCADE,null=True)
    muncipality=models.ForeignKey(tbl_muncipality,on_delete=models.CASCADE,null=True)
    complaint_status=models.IntegerField(default=0)
    complaint_date=models.DateField(auto_now_add=True)