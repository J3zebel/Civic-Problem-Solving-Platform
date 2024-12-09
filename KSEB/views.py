from django.shortcuts import render,redirect
from Guest.models import *
from django.conf import settings

# Create your views here.
def homepage(request):
    return render(request, "KSEB/Homepage.html")

def myprofile(request):
    kseb=tbl_kseb.objects.get(kseb_id=request.session['kid'])
    return render(request, "KSEB/MyProfile.html",{'kseb':kseb})


def editprofile(request):
    kseb=tbl_kseb.objects.get(kseb_id=request.session['kid'])
    if request.method=="POST":
        kseb.kseb_name=request.POST.get("txt_name")
        kseb.kseb_email=request.POST.get("txt_email")
        kseb.kseb_contact=request.POST.get("txt_contact")
        kseb.kseb_address=request.POST.get("txt_address")
        kseb.save()
        return redirect('KSEB:myprofile')
    else:
        return render(request, "KSEB/EditProfile.html",{'kseb':kseb})

    

def changepassword(request):
    kseb=tbl_kseb.objects.get(kseb_id=request.session['kid'])
    if request.method=="POST":
        pswd=kseb.kseb_password
        old=request.POST.get("old")
        new=request.POST.get("new")
        retype=request.POST.get("retype")
        if pswd == old:
            if new == retype:
                kseb.kseb_password=new
                kseb.save()
                return redirect('KSEB:myprofile')
            else:
                return render(request,"KSEB/ChangePassword.html",{'msg':"Password Mismatch"})
        else:
            return render(request,"KSEB/ChangePassword.html",{'msg':"Invalid Password"})
    else:
        return render(request, "KSEB/ChangePassword.html")
