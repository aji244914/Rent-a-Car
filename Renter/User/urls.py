from django.urls import path,include
from User import views
app_name="User"

urlpatterns = [
    
    path('Homepage/',views.Homepage,name='Homepage'),
path('Myprofile/',views.Myprofile,name='Myprofile'),
path('Editprofile/',views.Editprofile,name='Editprofile'),
path('Changepassword/',views.Changepassword,name='Changepassword'),

path('PostComp/',views.PostComp,name='PostComp'),
path("deletecomp/<int:aid>",views.deletecomp,name="deletecomp"),

path('ViewVehicle/',views.ViewVehicle,name='ViewVehicle'),

path('Gallery/<int:id>',views.Gallery,name='Gallery'),
path('Feedback/' ,views.Feedback,name='Feedback'),
path('Request/<int:id>',views.Request,name='Request'),
path('MyBooking/',views.MyBooking,name="MyBooking"),
path('Payment/<int:id>',views.Payment,name="Payment"),
path('PaymentSuccess/',views.PaymentSuccess,name="PaymentSuccess"),

path('rating/<int:mid>',views.rating,name="rating"),
path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
path('starrating/',views.starrating,name="starrating"),
path('logout/',views.logout,name="logout"),

]