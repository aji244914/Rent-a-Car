from django.urls import path,include
from Basics import views

urlpatterns = [
    path('add/',views.add,name='add'),
    path('Largest/',views.Largest,name='Largest'),
    path('ranklist/',views.ranklist,name='ranklist'),
    path('Armstrong/',views.armstrong,name='Armstrong'),
]
