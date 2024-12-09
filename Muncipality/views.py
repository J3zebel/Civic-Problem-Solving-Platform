from django.shortcuts import render,redirect
from Guest.models import *
from django.conf import settings

# Create your views here.
def homepage(request):
    return render(request, "Muncipality/Homepage.html")

def myprofile(request):
    mun=tbl_muncipality.objects.get(mun_id=request.session['mid'])
    return render(request, "Muncipality/MyProfile.html",{'mun':mun})


def editprofile(request):
    mun=tbl_muncipality.objects.get(mun_id=request.session['mid'])
    if request.method=="POST":
        mun.mun_name=request.POST.get("txt_name")
        mun.mun_email=request.POST.get("txt_email")
        mun.mun_contact=request.POST.get("txt_contact")
        mun.mun_address=request.POST.get("txt_address")
        mun.save()
        return redirect('Muncipality:myprofile')
    else:
        return render(request, "Muncipality/EditProfile.html",{'mun':mun})

    

def changepassword(request):
    mun=tbl_muncipality.objects.get(mun_id=request.session['mid'])
    if request.method=="POST":
        pswd=mun.mun_password
        old=request.POST.get("old")
        new=request.POST.get("new")
        retype=request.POST.get("retype")
        if pswd == old:
            if new == retype:
                mun.mun_password=new
                mun.save()
                return redirect('mun:myprofile')
            else:
                return render(request,"Muncipality/ChangePassword.html",{'msg':"Password Mismatch"})
        else:
            return render(request,"Muncipality/ChangePassword.html",{'msg':"Invalid Password"})
    else:
        return render(request, "Muncipality/ChangePassword.html")
