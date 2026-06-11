from Guest.models import   *
from django.shortcuts import render,redirect
from Admin.models import *

def Login(request):
    if request.method =="POST":
        Admincount=tbl_Admin.objects.filter(Admin_Email=request.POST.get("txt_email"),Admin_Password=request.POST.get("txt_pwd")).count()
        Usercount=tbl_user.objects.filter(User_Email=request.POST.get("txt_email"),User_Password=request.POST.get("txt_pwd")).count()
        rentercount=tbl_Renter.objects.filter(Renter_Email=request.POST.get("txt_email"),Renter_Password=request.POST.get("txt_pwd")).count()
        if Admincount>0:
            Admin=tbl_Admin.objects.get(Admin_Email=request.POST.get("txt_email"),Admin_Password=request.POST.get("txt_pwd"))
            request.session["gid"]=Admin.id
            return redirect("Admin:Homepage")
        elif Usercount>0:
            User=tbl_user.objects.get(User_Email=request.POST.get("txt_email"),User_Password=request.POST.get("txt_pwd"))
            request.session["uid"]=User.id
            return redirect("User:Homepage")
        elif rentercount>0:
            Renter=tbl_Renter.objects.get(Renter_Email=request.POST.get("txt_email"),Renter_Password=request.POST.get("txt_pwd"))
            request.session["rid"]=Renter.id
            return redirect("Renter:Homepage")

        else:
            return render(request,'Guest/Login.html',{'msg':'Account not found'})
        
    else:
        return render(request,'Guest/Login.html')
    
    
def UserRegistration(request):
    distdata=tbl_district.objects.all()
    if request.method =="POST":
        dis=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_user.objects.create(User_name=request.POST.get("txt_name"),User_Email=request.POST.get("txt_email"),User_contact=request.POST.get("txt_cnt"),User_address=request.POST.get("txt_area"),User_Password=request.POST.get("txt_pwd"),place=dis,User_photo=request.FILES.get("filephoto"))
        return redirect("Guest:UserRegistration")
    else:
        return render(request,'Guest/UserRegistration.html',{'distdata':distdata})
    
def ajaxplace(request):
        district=tbl_district.objects.get(id=request.GET.get("did"))
        place=tbl_place.objects.filter(district=district)
        return render(request,"Guest/Ajaxplace.html",{'place':place})

def renter(request):
    distdata=tbl_district.objects.all()
    us=tbl_Renter.objects.all()
    if request.method =="POST":
        dis=tbl_place.objects.get(id=request.POST.get("sel_place"))
        tbl_Renter.objects.create(Renter_name=request.POST.get("txt_name"),Renter_Email=request.POST.get("txt_email"),Renter_contact=request.POST.get("txt_cnt"),Renter_address=request.POST.get("txt_area"),Renter_Password=request.POST.get("txt_pwd"),place=dis,Renter_photo=request.FILES.get("filephoto"),Renter_proof=request.FILES.get("filephoto1"))
        return redirect("Guest:renter")
    else:
        return render(request,'Guest/RenterRegistration.html',{'distdata':distdata})
    

def Loginrent(request):
    if request.method =="POST":
        rentercount=tbl_Renter.objects.filter(Renter_Email=request.POST.get("txt_email"),Renter_Password=request.POST.get("txt_pwd")).count()
        Usercount=tbl_user.objects.filter(User_Email=request.POST.get("txt_email"),User_Password=request.POST.get("txt_pwd")).count()
        if rentercount>0:
            Admin=tbl_Renter.objects.get(Admin_Email=request.POST.get("txt_email"),Admin_Password=request.POST.get("txt_pwd"))
            request.session["gid"]=Admin.id
            return redirect("Admin:Homepage")
        elif Usercount>0:
            User=tbl_user.objects.get(User_Email=request.POST.get("txt_email"),User_Password=request.POST.get("txt_pwd"))
            request.session["uid"]=User.id
            return redirect("User:Homepage")

        else:
            return render(request,'Guest/Login.html',{'msg':'invalid'})
        
    else:
        return render(request,'Guest/Login.html')
    
def index(request):
    return render(request,'Guest/index.html')
    