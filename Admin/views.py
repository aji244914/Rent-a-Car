from Admin.models import   *
from Guest.models import   *
from User.models import   *
from datetime import datetime
from django.shortcuts import render,redirect

# Create your views here.
def District(request):
    dis=tbl_district.objects.all()
    if request.method =="POST":
        tbl_district.objects.create(district_name=request.POST.get("dist1"))
        return redirect("Admin:District")
    else:
        return render(request,'Admin/District.html',{'district':dis})
def deletedistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:District")
def editdistrict(request,aid):
    dis=tbl_district.objects.get(id=aid)
    if request.method=="POST":
        dis.district_name=request.POST.get("dist1")
        dis.save()
        return redirect("Admin:District")
    else:
        return render(request,'Admin/District.html',{'dist':dis})

def Admin(request):
    adm=tbl_Admin.objects.all()
    if request.method=="POST":
            name=request.POST.get("txt_name",)
            email=request.POST.get("txt_email")
            password=request.POST.get("txt_pwd")
            tbl_Admin.objects.create(Admin_name=name,Admin_Email=email,Admin_Password=password)
            return redirect("Admin:AdminRegistration")
    else:
        return render(request,'Admin/AdminRegistration.html',{'Admin':adm})
def deleteadmin(request,aid):
    tbl_Admin.objects.get(id=aid).delete()
    return redirect("Admin:AdminRegistration")
def editadmin(request,aid):
    adm=tbl_Admin.objects.get(id=aid)
    if request.method=="POST":
        adm.Admin_name=request.POST.get("txt_name")
        adm.Admin_Email=request.POST.get("txt_email")
        adm.Admin_Password=request.POST.get("txt_pwd")
        adm.save()
        return redirect("Admin:AdminRegistration")
    else:
        return render(request,'Admin/AdminRegistration.html',{'admi':adm})


def Category(request):
    cat=tbl_Category.objects.all()
    if request.method=="POST":
        tbl_Category.objects.create(Category_name=request.POST.get("txt_cat2"))
        return redirect("Admin:Category")
    else:
        return render(request,'Admin/Category.html',{'Category':cat})
def deletecat(request,aid):
    tbl_Category.objects.get(id=aid).delete()
    return redirect("Admin:Category")
def editcat(request,aid):
    esub=tbl_Category.objects.get(id=aid)
    if request.method=="POST":
        esub.Category_name=request.POST.get("txt_cat2")
        esub.save()
        return redirect("Admin:Category")
    else:
        return render(request,'Admin/Category.html',{'cat':esub})

    
    
def place(request):
    dis=tbl_district.objects.all()
    pl=tbl_place.objects.all()
    if request.method=="POST":
        dist=tbl_district.objects.get(id=request.POST.get("district"))
        tbl_place.objects.create(place_name=request.POST.get("txt_place"),district=dist)
        return redirect("Admin:Place")
    else:
        return render(request,'Admin/Place.html',{'seld':dis,'selp':pl})
def deleteplace(request,aid):
    tbl_place.objects.get(id=aid).delete()
    return redirect("Admin:Place")
def editplace(request,aid):
    dis=tbl_district.objects.all()
    plac=tbl_place.objects.get(id=aid)
    if request.method=="POST":
        plac.district=tbl_district.objects.get(id=request.POST.get("district"))
        plac.place_name=request.POST.get("txt_place")
        plac.save()
        return redirect("Admin:Place")
    else:
        return render(request,'Admin/Place.html',{'placi':plac,'seld':dis})
    


def SubCategory(request):
    catec=tbl_Category.objects.all()
    sc1=tbl_SubCategory.objects.all()
    if request.method=="POST":
            categ=tbl_Category.objects.get(id=request.POST.get("category"))
            tbl_SubCategory.objects.create(Subcategory_name=request.POST.get("txt_sub"),category=categ)
            return redirect("Admin:SubCategory")
    return render(request,'Admin/SubCategory.html',{'selc':catec,'selp':sc1})
def deletesub(request,aid):
    tbl_SubCategory.objects.get(id=aid).delete()
    return redirect("Admin:SubCategory")
def editsub(request,aid):
    esub=tbl_SubCategory.objects.get(id=aid)
    if request.method=="POST":
        esub.Subcategory_name=request.POST.get("txt_sub")
        esub.save()
        return redirect("Admin:SubCategory")
    else:
        return render(request,'Admin/SubCategory.html',{'esubi':esub})


def Homepage(request):
    adm=tbl_Admin.objects.get(id=request.session["gid"])
    adm=tbl_Admin.objects.all()
    return render(request,'Admin/Homepage.html')

def vehicletype(request):
    vt=tbl_vehicletype.objects.all()
    if request.method=="POST":
        tbl_vehicletype.objects.create(vehicletype_name=request.POST.get("txt_cat2"))
        return redirect("Admin:vehicletype")
    else:
        return render(request,'Admin/Vehicletype.html',{'Vehicletype':vt})
def deletevtype(request,aid):
    tbl_vehicletype.objects.get(id=aid).delete()
    return redirect("Admin:vehicletype")

def UserList(request):
    User=tbl_user.objects.all()
    return render(request,'Admin/UserList.html',{'User':User})


def Reply(request,id):
    repuser=tbl_Complaint.objects.get(id=id)
    if request.method=="POST":
        repuser.complaint_reply=request.POST.get("txtreplay")
        repuser.complaint_status=1
        repuser.complaint_replydate=datetime.now()
        repuser.save()
        return redirect("Admin:Viewcomp")
    else:
        return render(request,'Admin/Reply.html')


def Viewcomp(request):
    comp1=tbl_Complaint.objects.filter(complaint_status=0)
    replied=tbl_Complaint.objects.filter(complaint_status=1)
    return render(request,'Admin/ViewComplaint.html',{'comp1':comp1,'replied':replied})

def Renterlist(request):
    rentr=tbl_Renter.objects.filter(Renter_status=0)
    accept=tbl_Renter.objects.filter(Renter_status=1)
    reject=tbl_Renter.objects.filter(Renter_status=2)
    return render(request, 'Admin/Renterlist.html', {'renter': rentr,'accept':accept,'reject':reject})

def accept(request,id):
    rentr=tbl_Renter.objects.get(id=id)
    rentr.Renter_status=1
    rentr.save()
    return redirect("Admin:Renterlist")

def reject(request,id):
    rentr=tbl_Renter.objects.get(id=id)
    rentr.Renter_status=2
    rentr.save()
    return redirect("Admin:Renterlist")

def report(request):
    if request.method=="POST":
        renter = tbl_Renter.objects.all()
        for i in renter:
            i.count = tbl_Request.objects.filter(Request_fordate__gte=request.POST.get("txt_from_date"),Request_fordate__lte=request.POST.get("txt_to_date"),Request_status=4,vehicle__renter=i.id).count()
            return render(request,'Admin/Report.html',{"renter":renter})
    else:
        return render(request,'Admin/Report.html')

def logout(request):
    del request.session["gid"]
    return redirect("Guest:index")