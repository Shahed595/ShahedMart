from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    
    
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgetPassword/', views.forgetPassword, name='forgetPassword'),
    path('resetPasswordValidate/<uidb64>/<token>/', views.resetPasswordValidate, name='resetPasswordValidate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]
