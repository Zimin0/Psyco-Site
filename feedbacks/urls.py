from django.urls import path
from feedbacks.views import feedback

app_name = 'feedbacks'

urlpatterns = [
    path('send-feedback/', feedback, name="feedback"),
]