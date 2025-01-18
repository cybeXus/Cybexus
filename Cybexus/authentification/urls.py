
from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', lambda request: redirect('sign_in')),  # Redirige vers 'sing_in' par défaut
    path('sign_in/', views.sign_in , name = 'sign_in'), 
    path('login/', views.user_login, name = 'login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='authentification/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentification/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentification/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentification/password_reset_complete.html'), name='password_reset_complete')

]