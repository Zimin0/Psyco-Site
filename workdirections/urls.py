from django.urls import path

from workdirections.views import *

urlpatterns = [
    path('direction/<str:template_slug>/', one_direction, name='one_direction'),
    path('directions/ ', directions, name='directions'), 
]
