from django.db import models
from User.models import *

# Create your models here.

class tbl_updates(models.Model):
    update_content=models.CharField(max_length=100)
    complaint=models.ForeignKey(tbl_complaint,on_delete=models.CASCADE)
    update_date=models.DateField(auto_now_add=True)