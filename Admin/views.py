from django.shortcuts import render,redirect
from Admin.models import *

# Create your views here.
def sum(request):
    if request.method=="POST":
        Num1=int(request.POST.get('number 1'))
        Num2=int(request.POST.get('number 2'))
        btn=request.POST.get('btn')
        if btn=="+":
            Result= Num1 + Num2
        elif btn=="-":
            Result=Num1 - Num2
        elif btn=="*":
            Result=Num1 * Num2
        elif btn=="/":
            Result=Num1 / Num2
        elif btn=="%":
            Result=Num1 % Num2
        return render(request,'Admin/Sum.html',{'result':Result})
    else:
        return render(request,'Admin/Sum.html')
    
def largest(request):
        if request.method=="POST":
            Num1=int(request.POST.get('number1'))
            Num2=int(request.POST.get('number2'))
            Num3=int(request.POST.get('number3'))
            if Num1>Num2 and Num1>Num3:
                largest=Num1
            elif Num2>Num1 and Num2>Num3:
                largest=Num2
            elif Num3>Num1 and Num3>Num2:
                largest=Num3

            if Num1<Num2 and Num1<Num3:
                smallest=Num1
            elif Num2<Num1 and Num2<Num3:
                smallest=Num2
            elif Num3<Num1 and Num3<Num2:
                smallest=Num3
            return render(request,'Admin/Largest.html',{'result':largest,'smallest':smallest})
        else:
            return render(request,'Admin/Largest.html')

def salary(request):
    
    if request.method=="POST":
        Fname=(request.POST.get('f_name'))
        Lname=(request.POST.get('l_name'))
        Gender=(request.POST.get('Gender'))
        martial=(request.POST.get('martial'))   
        Dept=(request.POST.get('sel_dept'))
        Salary=int(request.POST.get('b_sal'))
        fullname= Fname + Lname
        if Gender=="male":
            name='Mr.'+fullname
            
        elif Gender=="female" and martial=="single":
            name='Miss.'+fullname
        elif Gender=="female" and martial=="married":
            name='Mrs.'+fullname
        if(Salary>=10000):
            ta=0.40*Salary
            da=0.35*Salary
            hra=0.30*Salary
            lic=0.25*Salary
            pf=0.20*Salary
        elif(Salary>=5000 and Salary<10000):
            ta=0.35*Salary
            da=0.30*Salary
            hra=0.25*Salary
            lic=0.20*Salary
            pf=0.15*Salary
        elif(Salary<5000):
            ta=0.3*Salary
            da=0.25*Salary
            hra=0.2*Salary
            lic=0.15*Salary
            pf=0.10*Salary
        Deduction=lic+pf
        net=Salary+ta+da+hra-(Deduction)
        return render(request,'Admin/Salary.html',{'name':name,'gender':Gender,'martial':martial,'dept':Dept,'salary':Salary,'ta':ta,'da':da,'hra':hra,'lic':lic,'pf':pf,'deduction':Deduction,'net':net})
    else:
         return render(request,'Admin/Salary.html')
    

def district(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get("district")
        tbl_district.objects.create(
            district_name=district
        )
        return render(request,'Admin/District.html',{'msg':"Data Inserted Successfully",'district':dis})
    else:
        return render(request,'Admin/District.html',{'district':dis})

def category(request):
    cat=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get("category")
        tbl_category.objects.create(
            category_name=category
        )
        return render(request,'Admin/category.html',{'msg':"Data Inserted",'cat':cat})
    else:
        return render(request,'Admin/category.html',{'cat':cat})
    
def admin(request):
    sel=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        pswd=request.POST.get("pswd")
        tbl_admin.objects.create(
            admin_name=name,admin_email=email,admin_pswd=pswd
        )
        msg="Data Inserted"
        return render(request,'Admin/Admin.html',{'msg':msg,'admin':sel})
    else:
        return render(request,'Admin/Admin.html',{'admin':sel})
    

def deladmin(request,id):
    tbl_admin.objects.get(id=id).delete()
    return redirect("Admin:admin")

def editadmin(request,id):
    edadm=tbl_admin.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        pswd=request.POST.get("pswd")
        edadm.admin_name=name
        edadm.admin_email=email
        edadm.admin_pswd=pswd
        edadm.save()
        return redirect("Admin:Admin")
    else:
        return render(request,"Admin/Admin.html",{'edit':edadm})

    

def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:district")

def editdistrict(request,id):
    ed=tbl_district.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("district")
        ed.district_name=name
        ed.save()
        return redirect("Admin:district")
    else:
        return render(request,"Admin/District.html",{'edit':ed})


def delcategory(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:category")

def place(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get("district"))
        place=request.POST.get("place")
        tbl_place.objects.create(district=district,place_name=place)
        return redirect("Admin:place")
    else:
        return render(request,'Admin/Place.html',{'district':dis})

def subcategory(request):
    sub=tbl_subcategory.objects.all()
    category=tbl_category.objects.all()
    if request.method=="POST":
        cat=tbl_category.objects.get(id=request.POST.get("category"))
        subcat=request.POST.get("subcategory")
        tbl_subcategory.objects.create(category=cat,sub_name=subcat)
        return render(request,'Admin/Subcategory.html',{'msg':"Data Inserted"})
    else:
        return render(request,'Admin/Subcategory.html',{'subcategory':sub,'category':category})
    
def delsub(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:subcategory")

def editsub(request,id):
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
        cat=request.POST.get("category")
        subcat=request.POST.get("subcategory")
        category.category_name=cat
        category.sub_category_name=subcat 
        category.save()
        return redirect("Admin:editsub")
    else:
        return render(request,"Admin/Subcategory.html",{'cat':category,'edit':subcategory})

def localplace(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        local=request.POST.get("local")
        tbl_localplace.objects.create(place=place,local_place=local)
        return render(request,'Admin/Localplace.html',{'msg':"Data Inserted"})
    else:
        return render(request,'Admin/Localplace.html',{'district':dis})
    