from django.urls import path,include
from Renter import views
app_name="Renter"

urlpatterns = [
    
    path('Homepage/',views.Homepage,name='Homepage'),
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),
    
    
    path('VehicleRegistration/',views.VehicleRegistration,name='VehicleRegistration'),
    path("deleteveh/<int:aid>",views.deleteveh,name="deleteveh"),
    
    path('AddGallery/<int:id>',views.AddGallery,name='AddGallery'),
    path("deletegallery/<int:aid>/<int:id>",views.deletegallery,name="deletegallery"),
    
    path('ViewBooking/',views.ViewBooking,name="ViewBooking"),
    path('Startkm/<int:id>',views.Startkm,name='Startkm'),
    path('rejectreq/<int:id>',views.rejectreq,name='rejectreq'),
    path('Endkm/<int:id>',views.Endkm,name='Endkm'),

    path('logout/',views.logout,name="logout"),
    
]