from django.urls import path

from home.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about-me/ ', about, name='about'),
    path('about/', about, name='about'),
    path('work_directions/', work_directions, name='work_directions'),
    path('cooperation/', cooperation, name='cooperation'),
    path('contacts/', contacts, name='contacts'),
]
