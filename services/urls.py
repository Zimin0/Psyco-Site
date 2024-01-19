from django.urls import path

from home.views import *

urlpatterns = [
    path('services-and-prices/', services, name="services")    
]
