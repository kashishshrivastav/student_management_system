from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.http import HttpResponse
# import required package
import re
# Create your views here.
def index(request):
    return render(request,'index.html')

def courses(request):
    course_obj = Course.objects.all()
    return render(request,'courses.html',{'course_obj':course_obj})

def addcourse(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        fees = request.POST.get('fees')
        duration = request.POST.get('duration')
        if Course.objects.filter(course_name=course_name).exists():
            messages.error(request,'already exists')
        else:
            Course.objects.create(course_name=course_name,fees=fees,duration=duration)
            messages.success(request,'course added successfully')
            return redirect('/courses/')

def dashboard(request):
    return render(request,'dashboard.html')

def viewstudents(request):
    return render(request,'viewstudents.html')

def sign_up(request):
    return render(request,'sign-up.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already registered')
            return redirect('/signup/')
        else:   
            if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", password):
                    User.objects.create(name=name,email=email,password=password)
                    messages.success(request,"user registred successfullyy")
                    return redirect('/')       
            else:
                messages.error(request,'create strong password')
                return redirect('/signup/')
        
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        userpassword = request.POST['password']
        if User.objects.filter(email=email).exists():
           obj = User.objects.get(email=email)
           password = obj.password
           if check_password(userpassword,password):
               return redirect('/dashboard/')
           else:
               messages.error(request,'password incorrect')
               return redirect('/')
        else:
            messages.error(request,'email not registered')
            return redirect('/')
        
