from django.shortcuts import render,redirect
from Guest.models import *
from django.conf import settings

# Create your views here.
def homepage(request):
    return render(request, "PWD/Homepage.html")

def myprofile(request):
    pwd=tbl_pwd.objects.get(pwd_id=request.session['pid'])
    return render(request, "PWD/MyProfile.html",{'pwd':pwd})


def editprofile(request):
    pwd=tbl_pwd.objects.get(pwd_id=request.session['pid'])
    if request.method=="POST":
        pwd.pwd_name=request.POST.get("txt_name")
        pwd.pwd_email=request.POST.get("txt_email")
        pwd.pwd_contact=request.POST.get("txt_contact")
        pwd.pwd_address=request.POST.get("txt_address")
        pwd.save()
        return redirect('PWD:myprofile')
    else:
        return render(request, "PWD/EditProfile.html",{'pwd':pwd})

    

def changepassword(request):
    pwd=tbl_pwd.objects.get(pwd_id=request.session['pid'])
    if request.method=="POST":
        pswd=pwd.pwd_password
        old=request.POST.get("old")
        new=request.POST.get("new")
        retype=request.POST.get("retype")
        if pswd == old:
            if new == retype:
                pwd.pwd_password=new
                pwd.save()
                return redirect('PWD:myprofile')
            else:
                return render(request,"PWD/ChangePassword.html",{'msg':"Password Mismatch"})
        else:
            return render(request,"PWD/ChangePassword.html",{'msg':"Invalid Password"})
    else:
        return render(request, "PWD/ChangePassword.html")
