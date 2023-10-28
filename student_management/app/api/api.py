from .serializers import *
from app.models import *
from rest_framework import generics
from rest_framework.response import Response

class RegistrationViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class RegistrationShowViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class CourseViewSet(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseShowViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer