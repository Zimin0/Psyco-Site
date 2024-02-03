from django.urls import path
from services.views import *

app_name = 'services'

urlpatterns = [
    path('services-and-prices/', services, name="services"),
    path('services/<int:id>', service, name="service"), 
]
