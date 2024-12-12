from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from django.conf import settings

# Create your views here.
def homepage(request):
    return render(request, "MVD/Homepage.html")

def myprofile(request):
    mvd=tbl_mvd.objects.get(mvd_id=request.session['mid'])
    return render(request, "MVD/MyProfile.html",{'mvd':mvd})


def editprofile(request):
    mvd=tbl_mvd.objects.get(mvd_id=request.session['mid'])
    if request.method=="POST":
        mvd.mvd_name=request.POST.get("txt_name")
        mvd.mvd_email=request.POST.get("txt_email")
        mvd.mvd_contact=request.POST.get("txt_contact")
        mvd.mvd_address=request.POST.get("txt_address")
        mvd.save()
        return redirect('MVD:myprofile')
    else:
        return render(request, "MVD/EditProfile.html",{'mvd':mvd})

    

def changepassword(request):
    mvd=tbl_mvd.objects.get(mvd_id=request.session['mid'])
    if request.method=="POST":
        pswd=mvd.mvd_password
        old=request.POST.get("old")
        new=request.POST.get("new")
        retype=request.POST.get("retype")
        if pswd == old:
            if new == retype:
                mvd.mvd_password=new
                mvd.save()
                return redirect('MVD:myprofile')
            else:
                return render(request,"MVD/ChangePassword.html",{'msg':"Password Mismatch"})
        else:
            return render(request,"MVD/ChangePassword.html",{'msg':"Invalid Password"})
    else:
        return render(request, "MVD/ChangePassword.html")
    

def viewcomplaint(request):
    mvd=tbl_mvd.objects.get(mvd_id=request.session['mid']) 
    complaint=tbl_complaint.objects.filter(mvd_id=mvd)
    return render(request, "MVD/Viewcomplaint.html",{'complaint':complaint})

def reply(request,id):
    complaint=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        complaint.complaint_response=request.POST.get("txt_reply")
        complaint.complaint_status="1"
        complaint.save()
        return redirect("MVD:viewcomplaint")
    else:
        return render(request, "MVD/Reply.html")
