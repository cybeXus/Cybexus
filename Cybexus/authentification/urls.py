
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('sign_in')),  # Redirige vers 'sing_in' par défaut
    path('sign_in/', views.sign_in , name = 'sign_in'), 
    path('login/', views.user_login, name = 'login'),

]