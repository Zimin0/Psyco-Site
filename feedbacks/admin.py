from django.contrib import admin

from feedbacks.models import Feedback

@admin.register(Feedback)
class FeedbackADmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'problem_discription']
