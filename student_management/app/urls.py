from django.contrib import admin
from django.urls import path,include
from app.api.api import *
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
    path('addstudent/',views.addstudent),
    path('delete_student/<int:pk>/',views.delete_student),
    path('update_page/<int:pk>/',views.update_page),
    path('updatestudent/',views.update_view),
    path('search/',views.search,name='search'),
    path('viewtrainers/',views.viewtrainers),
    path('addtrainer/',views.addtrainer),
    # api urls
    path('reg/',RegistrationViewSet.as_view()),
    path('show/',RegistrationShowViewSet.as_view()),
    path('courseapi/',CourseViewSet.as_view()),
    path('showcourse/',CourseShowViewSet.as_view()),
    path('addstudentapi/',StudentViewSet.as_view()),
    path('showdetails/',StudentShowViewSet.as_view()),
    path('showId/<int:pk>/',RegistrationIdViewSet.as_view()),
    path('updateuser/<int:pk>/',RegistrationUpdateViewSet.as_view()),
    path('deleteapi/<int:pk>/',RegistrationDeleteViewSet.as_view())
]