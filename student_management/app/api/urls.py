from django.urls import path
from .api import *

urlpatterns =  [
    path('reg/',RegistrationViewSet.as_view())
]
