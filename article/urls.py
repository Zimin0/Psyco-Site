from django.urls import path

from article.views import *

app_name = 'article'

urlpatterns = [
    path('article/<int:id>/', article, name='article'),
]
