from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def courses(request):
    return render(request,'courses.html')

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
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already registered')
            return redirect('/signup/')
        else:
            User.objects.create(name=name,email=email,password=password)
            return redirect('/')
        
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
               return redirect('/login/')
        else:
            messages.error(request,'email not registered')