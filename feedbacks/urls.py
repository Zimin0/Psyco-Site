from django.urls import path
from feedbacks.views import feedback

urlpatterns = [
    path('send-feedback/', feedback, name="feedback"),
]