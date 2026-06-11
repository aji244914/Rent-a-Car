from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [
    path('login/',views.Login,name='login'),
    path('UserRegistration/',views.UserRegistration,name='UserRegistration'),
    path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('renter/',views.renter,name='renter'),
    path('',views.index,name='index'),
    
    
]