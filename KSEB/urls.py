from django.urls import path
from KSEB import views
app_name="KSEB"

urlpatterns = [
    path('Homepage/',views.homepage,name="homepage"),
    path('My Profile/',views.myprofile,name="myprofile"),
    path('Edit Profile/',views.editprofile,name="editprofile"),
    path('Change Password/',views.changepassword,name="changepassword"),
    path('View Complaint/',views.viewcomplaint,name="viewcomplaint"),
    path('Reply/<int:id>',views.reply,name="reply"),
    path('updates/<int:id>',views.update,name="updates"),
]