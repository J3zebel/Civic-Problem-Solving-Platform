from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=40)
    admin_pswd=models.CharField(max_length=30)

class tbl_place(models.Model):
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
    place_name=models.CharField(max_length=30)

class tbl_subcategory(models.Model):
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    sub_name=models.CharField(max_length=30)

class tbl_localplace(models.Model):
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    local_place=models.CharField(max_length=30)