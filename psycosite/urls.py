from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('article.urls')),
    path('', include('services.urls')),
    path('', include('feedbacks.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
