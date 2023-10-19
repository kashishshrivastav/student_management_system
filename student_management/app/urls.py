from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('courses/',views.courses),
    path('addcourse/',views.addcourse),
    path('dashboard/',views.dashboard),
    path('viewstudents/',views.viewstudents),
    path('signup/',views.sign_up),
    path('registration/',views.registration),
    path('login_user/',views.login),
    path('addstudent/',views.addstudent)
    
]