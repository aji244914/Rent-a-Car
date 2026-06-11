from Guest.models import   *
from Admin.models import   *
from User.models import   *
from Renter.models import   *
from django.shortcuts import render,redirect
from django.http import JsonResponse
# Create your views here.
def Homepage(request):
    return render(request,'User/Homepage.html')
def Myprofile(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    
    
    return render(request,'User/Myprofile.html',{'user':user})
def Editprofile(request):
    eu=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        eu.User_name=request.POST.get("txt_u1")
        eu.User_Email=request.POST.get("txt_u2")
        eu.User_contact=request.POST.get("txt_u3")
        eu.save()
        return redirect('User:Myprofile')
    else:
        return render(request,'User/Editprofile.html',{'user':eu})

def Changepassword(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    dbpass=user.User_Password
    if request.method=="POST":
        old=request.POST.get("txt_pwd1")
        new=request.POST.get("txt_pwd2")
        retype=request.POST.get("txt_pwd3")
        if dbpass==old:
            if new==retype:
                user.User_Password =new
                user.save()
                return redirect("User:Myprofile")
            else:
                return render(request,"User/Changepassword.html")
        else:
            return render(request,"User/Changepassword.html",{'msg':'invalid'})
    else:
        return render(request,'User/Changepassword.html')
    
def PostComp(request):
    comp=tbl_Complaint.objects.filter(User_id=request.session['uid'])
    if request.method =="POST":
        us=tbl_user.objects.get(id=request.session["uid"])
        
        tbl_Complaint.objects.create(Complaint_subject=request.POST.get("txt_cat2"),Complaint_complaint=request.POST.get("txt_area"),User_id=us)
        return redirect("User:PostComp")
    else:
        return render(request,'User/PostComplaint.html',{'comp':comp})
def deletecomp(request,aid):
    tbl_Complaint.objects.get(id=aid).delete()
    return redirect("User:PostComp")

def ViewVehicle(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    Us=tbl_Vehicle.objects.all()
    for i in Us:
        tot=0
        ratecount=tbl_rating.objects.filter(vehicle=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(vehicle=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(Us,parry)
    return render(request,'User/ViewVehicle.html',{"Vehicletype":datas,"ar":ar})

def Gallery(request,id):
    vehicle=tbl_VehicleGallery.objects.filter(vehicle=id)
    return render(request,'User/Gallery.html',{"Gallery":vehicle})

def Feedback(request):
    fee=tbl_feedback.objects.all()
    if request.method=="POST":
        feedbck=request.POST.get("txt_feedback")
        us=tbl_user.objects.get(id=request.session["uid"])
        tbl_feedback.objects.create(feedback_content=feedbck,user=us)
        return redirect("User:Feedback")
    else:
        return render(request,'User/Feedback.html',{'Feedback':fee})
    
def Request(request,id):
    if request.method=="POST":
        req=request.POST.get("txt_Date")
        vehicle=tbl_Vehicle.objects.get(id=id)
        requ=tbl_user.objects.get(id=request.session["uid"])
        tbl_Request.objects.create(Request_fordate=req,user=requ,vehicle=vehicle)
        return redirect("User:ViewVehicle")
    else:
        return render(request,'User/Request.html')

# def MyBooking(request,):
# #     Vb=tbl_booking.objects.all()
#     book=tbl_booking.objects.filter(user=request.session['uid'])
#     return render(request,'EventPlanner/ViewBooking.html',{"booking":book})
def MyBooking(request):
    book=tbl_Request.objects.filter(user=request.session['uid'])
    return render(request,'User/MyBooking.html',{"booking":book})

def Payment(request,id):
    req=tbl_Request.objects.get(id=id)
    amount = req.Request_amount
    if request.method=="POST":
        req.Request_status=4
        req.save()
        return redirect("User:PaymentSuccess")
    else:
        return render(request,'User/Payment.html',{'amount':amount})

def PaymentSuccess(request):
    return render(request,'User/PaymentSuccess.html')

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(vehicle=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(vehicle=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),user_review=user_review,rating_data=rating_data,vehicle=tbl_Vehicle.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(vehicle=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(vehicle=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(vehicle=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

def logout(request):
    del request.session["uid"]
    return redirect("Guest:index")