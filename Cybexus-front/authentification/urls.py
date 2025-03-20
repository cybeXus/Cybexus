from django.urls import path
from django.shortcuts import redirect
from . import views
from django.contrib.auth import views as auth_views  # Correct import for auth views
# No need to import CustomPasswordResetView here unless you're using it

urlpatterns = [
    path('', lambda request: redirect('sign_in')),  # Redirects to 'sign_in' by default
    path('sign_in/', views.sign_in , name='sign_in'), 
    path('login/', views.user_login, name='login'),

    # Password reset URLs using Django's default views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
