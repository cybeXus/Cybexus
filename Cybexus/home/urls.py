from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('formation/', views.formation, name="formation"),
    path('contact/', views.contact, name="contact"),
]
