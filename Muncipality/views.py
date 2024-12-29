from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from MVD.models import *
from django.db.models import Count
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
    
def viewcomplaint(request):
    muncipality=tbl_muncipality.objects.get(mun_id=request.session['mid']) 
    complaint=tbl_complaint.objects.filter(muncipality=muncipality).annotate(like_count=Count('tbl_like')).order_by('-like_count')
    return render(request,"Muncipality/Viewcomplaint.html",{'complaint':complaint})

def reply(request,id):
    complaint=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        complaint.complaint_response=request.POST.get("txt_reply")
        complaint.complaint_status="1"
        complaint.save()
        return redirect("Muncipality:viewcomplaint")
    else:
        return render(request, "Muncipality/Reply.html")
    

def update(request,id):
    if request.method=="POST":
        tbl_updates.objects.create(
            complaint=tbl_complaint.objects.get(id=id),
            update_content=request.POST.get("txt_reply")
        )
        return redirect("Muncipality:viewcomplaint")
    else:
        return render(request,'Muncipality/Update.html')
    
def viewreply(request):
    muncipality=tbl_muncipality.objects.get(mun_id=request.session['mid']) 
    request=tbl_request.objects.filter(muncipality=muncipality)
    return render(request,"Muncipality/Viewreply.html",{'reply':reply})