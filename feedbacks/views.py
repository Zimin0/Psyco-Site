from django.shortcuts import render
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback

from settings.upload_info import get_personal_data_from_db

def feedback(request):
    """ Форма обратной связи. """
    context = {}
    context.update(get_personal_data_from_db())

    if request.method == 'GET':
        form = FeedbackForm()
        context['form'] = form
        return render(request, "feedbacks/form.html", context)
    
    if request.method == 'POST':
        print(request.POST)
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = FeedbackForm()
        else:
            print("Форма невалидна!")
            print(form.errors)
            context['errors'] = form.errors
        context['form'] = form
        return render(request, "feedbacks/form.html", context)