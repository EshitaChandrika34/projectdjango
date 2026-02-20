from django.urls import path
from .views import student_register, success_page

urlpatterns = [
    path('register/', student_register, name='register'),
    path('success/', success_page, name='success'),
]
