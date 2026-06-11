from django.shortcuts import render,redirect
from Guest.models import  *
from Admin.models import *
from Renter.models import *
from User.models import *

# Create your views here.
def Homepage(request):
    return render(request,'Renter/Homepage.html')
def Myprofile(request):
    renter=tbl_Renter.objects.get(id=request.session["rid"])
    return render(request,'Renter/Myprofile.html',{'renter':renter})


def Editprofile(request):
    eu=tbl_Renter.objects.get(id=request.session["rid"])
    if request.method=="POST":
        eu.Renter_name=request.POST.get("txt_name")
        eu.Renter_Email=request.POST.get("txt_email")
        eu.Renter_contact=request.POST.get("txt_cnt")
        eu.Renter_address=request.POST.get("txt_area")
        eu.save()
        return redirect('Renter:Myprofile')
    else:
        return render(request,'Renter/Editprofile.html',{'renter':eu})


def Changepassword(request):
    eu=tbl_Renter.objects.get(id=request.session["rid"])
    dbpass=eu.Renter_Password
    if request.method=="POST":
        old=request.POST.get("txt_pwd1")
        new=request.POST.get("txt_pwd2")
        retype=request.POST.get("txt_pwd3")
        if dbpass==old:
            if new==retype:
                eu.Renter_Password =new
                eu.save()
                return redirect("Renter:Myprofile")
            else:
                return render(request,"Renter/Changepassword.html")
        else:
            return render(request,"Renter/Changepassword.html",{'msg':'invalid'})
    else:
        return render(request,'Renter/Changepassword.html')
    

def VehicleRegistration(request):
    vehic=tbl_vehicletype.objects.all()
    vh=tbl_Vehicle.objects.filter(renter=request.session['rid'])
    if request.method =="POST":
        Vehicletype=tbl_vehicletype.objects.get(id=request.POST.get("sel_vehicle"))
        renter=tbl_Renter.objects.get(id=request.session["rid"])
        tbl_Vehicle.objects.create(Vehicle_name=request.POST.get("txt_veh"),Vehicle_minkm=request.POST.get("txt_km"),vehicletype=Vehicletype,Vehicle_minrate=request.POST.get("txt_rat"),Vehicle_kmrate=request.POST.get("txt_rat"),Vehicle_image=request.FILES.get("filephoto3"),renter=renter)
        return redirect("Renter:VehicleRegistration")
    else:
        return render(request,'Renter/VehicleRegistration.html',{'Vehicletype':vehic,'Vehicle':vh})
def deleteveh(request,aid):
    tbl_Vehicle.objects.get(id=aid).delete()
    return redirect("Renter:VehicleRegistration")

def AddGallery(request,id):
    vehi=tbl_VehicleGallery.objects.filter(vehicle=id)
    if request.method =="POST":
        vehicle=tbl_Vehicle.objects.get(id=id)
        tbl_VehicleGallery.objects.create(Vehicle_photo=request.FILES.get("filephoto4"),vehicle=vehicle)
        return redirect("Renter:AddGallery",id)
    else:
        return render(request,'Renter/AddGallery.html',{'Gallery':vehi,"id":id})
    
def deletegallery(request,aid,id):
    tbl_VehicleGallery.objects.get(id=aid).delete()
    return redirect("Renter:AddGallery",id)


def ViewBooking(request):
    vibook=tbl_Request.objects.filter(vehicle__renter=request.session['rid'])
    return render(request,'Renter/ViewBooking.html',{"vbooking":vibook})

def Startkm(request,id):
    data=tbl_Request.objects.get(id=id)
    if request.method =="POST":
        data.Request_startKm=request.POST.get("txt_skm")
        data.Request_status=1
        data.save()
        return redirect('Renter:ViewBooking')
    else:
        return render(request,'Renter/AddKilometer.html')

def rejectreq(request,id):
    data=tbl_Request.objects.get(id=id)
    data.Request_status=2
    data.save()
    return redirect('Renter:ViewBooking')

def Endkm(request,id):
    data=tbl_Request.objects.get(id=id)
    startkm = data.Request_startKm
    minrate = data.vehicle.Vehicle_minrate
    minkm = data.vehicle.Vehicle_minkm
    km = data.vehicle.Vehicle_kmrate
    if request.method =="POST":
        diff = int(request.POST.get("txt_ekm")) - int(startkm)
        if diff > int(minkm):
            bal  = diff - int(minkm)
            total = bal * int(km)
            data.Request_endKm=request.POST.get("txt_ekm")
            data.Request_amount = total
            data.Request_status=3
            data.save()
        else:
            data.Request_endKm=request.POST.get("txt_ekm")
            data.Request_amount = minrate
            data.Request_status=3
            data.save()
        return redirect('Renter:ViewBooking')
    else:
        return render(request,'Renter/EndKilometer.html')

def logout(request):
    del request.session["rid"]
    return redirect("Guest:index")