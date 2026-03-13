from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colleges/', views.colleges, name='colleges'),
    path('colleges/<slug:slug>/', views.college_detail, name='college_detail'),
    path('students/', views.students, name='students'),
    path('address/', views.address, name='address'),

    path('login/', views.login_page, name='login'),
    path('loginverification/', views.loginverification, name='loginverification'),
    path('SignupForm/', views.signup_form, name='SignupForm'),
     path('welcome/', views.welcome, name='welcome'),
]
