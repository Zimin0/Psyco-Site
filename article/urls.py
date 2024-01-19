from django.urls import path

from home.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('about-me/ ', about, name='about'),
    
]
