from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('',homepageview,name = "homepage"),
    path('logout/',logoutuser,name = "logout"),
    path('user/login/',userloginpage,name = "userloginpage"),
    path('user/login/validate/',userlogin,name = "userlogin"),
    path('user/homepage/',userhomepage,name = "userhomepage"),
    path('packagedetails/<int:taskid>/',packagedetails,name = "packagedetails"),
    path('vehicleselection/<int:taskid>/',vehicleselection,name = "vehicleselection"),
    path("hotles/<int:mybookingid>/<int:vehicleid>/",hotles, name="hotles"),
    path('addcoment/<int:taskid>/',addcoment, name = "addcoment"),
    path("summary/<int:mybookingid>/<int:hotelid>/",summary, name="summary"),



    


   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   
