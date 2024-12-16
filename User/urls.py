from django.urls import path
from User import views
app_name="User"

urlpatterns = [
    path('Homepage/',views.homepage,name="homepage"),
    path('MyProfile/',views.myprofile,name="myprofile"),
    path('EditProfile/',views.editprofile,name="editprofile"),
    path('ChangePassword/',views.changepassword,name="changepassword"),
    path('muncipalitycomplaint/<str:id>',views.muncipalitycomplaint,name="muncipalitycomplaint"),
    path('mvdcomplaint/<str:id>',views.mvdcomplaint,name="mvdcomplaint"),
    path('pwdcomplaint/<str:id>',views.pwdcomplaint,name="pwdcomplaint"),
    path('ksebcomplaint/<str:id>',views.ksebcomplaint,name="ksebcomplaint"),
    path('SearchMuncipality/',views.searchmunicipality,name="searchmunicipality"),
    path('ajaxsearchmunicipality/',views.ajaxsearchmunicipality,name="ajaxsearchmunicipality"),
    path('Searchmvd/',views.searchmvd,name="searchmvd"),
    path('ajaxsearchmvd/',views.ajaxsearchmvd,name="ajaxsearchmvd"),
    path('Searchpwd/',views.searchpwd,name="searchpwd"),
    path('ajaxsearchpwd/',views.ajaxsearchpwd,name="ajaxsearchpwd"),
    path('Searchkseb/',views.searchkseb,name="searchkseb"),
    path('ajaxsearchkseb/',views.ajaxsearchkseb,name="ajaxsearchkseb"),
    path('Feedback/',views.feedback,name="feedback"),
    path('Mycompliants/',views.mycomplaints,name="mycomplaints"),
    path('Updates/',views.updates,name="updates"),
    path('public/',views.publiccomplaint,name="publiccomplaint"),
    path('ajaxlike/',views.ajaxlike,name="ajaxlike"),
] 