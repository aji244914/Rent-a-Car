from django.urls import path,include
from Admin import views
app_name="Admin"

urlpatterns = [
    
    path('Homepage/',views.Homepage,name='Homepage'),
    
    path('District/',views.District,name='District'),
    path("deletedistrict/<int:id>",views.deletedistrict,name="deletedistrict"),
    path("editdistrict/<int:aid>",views.editdistrict,name="editdistrict"),
    
    path('AdminRegistration/',views.Admin,name='AdminRegistration'),
    path("deleteadmin/<int:aid>",views.deleteadmin,name="deleteadmin"),
    path("deleteadmin/<int:aid>",views.deleteadmin,name="deleteadmin"),
    path("editadmin/<int:aid>",views.editadmin,name="editadmin"),
    
    path('Place/',views.place,name='Place'),
    path("deleteplace/<int:aid>",views.deleteplace,name="deleteplace"),
    path("editplace/<int:aid>",views.editplace,name="editplace"),
    
    path('Category/',views.Category,name='Category'),
    path('SubCategory/',views.SubCategory,name='SubCategory'),
    path("deletesub/<int:aid>",views.deletesub,name="deletesub"),
    path("editsub/<int:aid>",views.editsub,name="editsub"),
    path("deletecat/<int:aid>",views.deletecat,name="deletecat"),
    path("editcat/<int:aid>",views.editcat,name="editcat"),
    
    path('vehicletype/',views.vehicletype,name='vehicletype'),
    path("deletevtype/<int:aid>",views.deletevtype,name="deletevtype"),
    
    path('UserList/',views.UserList,name='UserList'),
    
    path('Reply/<int:id>',views.Reply,name='Reply'),
    path('Viewcomp/',views.Viewcomp,name='Viewcomp'),
    
    path('Renterlist/',views.Renterlist,name='Renterlist'),
    path('accept/<int:id>',views.accept,name='accept'),
    path('reject/<int:id>',views.reject,name='reject'),
    path('report/',views.report,name='report'),
    path('logout/',views.logout,name="logout"),
]