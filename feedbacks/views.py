from django.shortcuts import render
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback

def feedback(request):
    """ Форма обратной связи. """
    if request.method == 'GET':
        form = FeedbackForm()
        return render(request, "feedbacks/form.html", {'form':form})
    
    if request.method == 'POST':
        print(request.POST)
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = FeedbackForm()
        else:
            print("Форма невалидна!")
            print(form.errors)
        return render(request, "feedbacks/form.html", {'form':form, 'errors':form.errors})