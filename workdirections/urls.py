from django.urls import path

from workdirections.views import *

app_name = 'workdirections'

urlpatterns = [
    path('directions/<int:index>', one_direction, name='one_direction'), 
]
