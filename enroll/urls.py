from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    
    path('data',views.datainsert)
]
