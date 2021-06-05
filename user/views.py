from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import *
# Create your views here.
def homepageview(request):
    packages=package.objects.all()
    context = {'packages' : packages}
    return render(request, "user/homepage.html",context)

def userloginpage(request):
    return render(request,"user/userloginpage.html")

def userlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        User.objects.filter(username = username)[0]
    except:
        messages.add_message(request, messages.INFO, "invalid credentials ! check username and password")
        return redirect("userloginpage")

    if userlogindata.objects.filter(user = User.objects.filter(username = username)[0]).exists():

        user = authenticate(username = username,password = password)

        if user is not None:
            login(request,user)
            return redirect("homepage")
    messages.add_message(request, messages.INFO, "invalid credentials ! check username and password")
    return redirect(request.META["HTTP_REFERER"])

def userhomepage(request):
    if request.user.is_superuser:
        messages.add_message(request,messages.INFO,"you must login as user")
        logout(request)
        return redirect("userloginpage")
    workunits = ["My feedbacks"]
    context = {'workunits' : workunits,'username' : request.user.username}
    return render(request,"user/userhomepage.html",context)

def logoutuser(request):
    logout(request)
    return redirect("homepage")

def packagedetails(request,taskid):
    pdata = package.objects.get(id=taskid)
    pcoments = comment.objects.filter(pakage=pdata)
    context = {'package' : pdata,"coments":pcoments,"pkgid":pdata.id}
    return render(request,"user/packagedetails.html",context)


def vehicleselection(request,taskid):
    source = request.POST['source']
    members = request.POST['members']
    fromdate = request.POST['fromdate']
    todate = request.POST['todate']
    pdata = package.objects.get(id=taskid)
    mbus = vehicletype.objects.get(vname='bus')
    mcar = vehicletype.objects.get(vname='car')
    print(request.user)
    user1 = userlogindata.objects.get(user=request.user)
    books = mybookings(user=user1,pakage=pdata,members=members,source=source,fromdate=fromdate,todate=todate)
    books.save()
    bus1 = vehicle.objects.filter(destination=pdata.pdestination).filter(mtype=mbus)
    car1 = vehicle.objects.filter(destination=pdata.pdestination).filter(mtype=mcar)
    print(books)
    context = {'mybooking' : books,"buss":bus1,"cars":car1}
    return render(request,"user/vehicalselection.html",context)

def hotles(request,mybookingid,vehicleid):
    print(mybookingid)
    print(vehicleid)
    mybookingss = mybookings.objects.get(id=mybookingid)
    veh = vehicle.objects.get(id=vehicleid)
    mybookingss.mvehicle=veh
    mybookingss.save()
    print(mybookingss.pakage.pdestination)
    hotelss = hotels.objects.filter(loaction=mybookingss.pakage.pdestination)
    context = {'mybooking' : mybookingss,"hotels":hotelss,"mybookingid":mybookingid}
    print(veh)
    print(hotelss)
    print(mybookingss)
    return render(request,"user/hotelselection.html",context)


def addcoment(request,taskid):
    comment1 = request.POST['comment']
    ratings = request.POST['rating']
    pdata = package.objects.get(id=taskid)
    user1 = userlogindata.objects.get(user=request.user)
    print(comment)
    print(ratings)
    print(pdata)
    print(user1)
    comentss = comment(user=user1,coment=comment1,cratings=ratings,pakage=pdata)
    comentss.save()
    return redirect('packagedetails', taskid=taskid)



def summary(request,mybookingid,hotelid):
    print(mybookingid)
    mybookingss = mybookings.objects.get(id=mybookingid)
    htl = hotels.objects.get(id=hotelid)
    mybookingss.mhotle=htl
    mybookingss.save()
    ppprice = mybookingss.pakage.price
    tvprice = mybookingss.mvehicle.vprice
    hhprice = mybookingss.mhotle.price
    membersss = mybookingss.members
    halfmem = membersss / 2
    thprice = halfmem * hhprice
    mbus = vehicletype.objects.get(vname='bus')                       
    if(mybookingss.mvehicle.mtype == mbus):
        tvprice = tvprice * membersss
    totalprice = ppprice + thprice + tvprice
    print(ppprice,tvprice,hhprice,membersss,halfmem,thprice,totalprice)
    print(mybookingss.pakage.pdestination)
    context = {'mybooking' : mybookingss,"mybookingid":mybookingid,"tvprice":tvprice,"thprice":thprice,"halfmem":halfmem,"tprice":totalprice}
    return render(request,"user/ordersummary.html",context)
