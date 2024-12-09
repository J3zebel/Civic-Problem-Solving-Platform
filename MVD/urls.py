from django.urls import path
from MVD import views
app_name="MVD"

urlpatterns = [
    path('Homepage/',views.homepage,name="homepage"),
    path('My Profile/',views.myprofile,name="myprofile"),
    path('Edit Profile/',views.editprofile,name="editprofile"),
    path('Change Password/',views.changepassword,name="changepassword"),
]