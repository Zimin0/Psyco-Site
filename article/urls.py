from django.urls import path

from article.views import *

urlpatterns = [
    path('article/<int:id>/', article, name='article'),
]
