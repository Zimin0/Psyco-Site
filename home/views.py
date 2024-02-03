from django.shortcuts import render, get_object_or_404
from settings.models import Setting
from settings.upload_info import get_personal_data_from_db

from article.models import Article

def home(request):
    """ Главная страница. """
    context = {}
    context['articles'] = Article.objects.filter()
    context.update(get_personal_data_from_db())
    return render(request, 'home/home.html', context)

def about(request):
    """ Обо мне. """
    context = {}
    context.update(get_personal_data_from_db())
    return render(request, 'home/about.html', context)

def work_directions(request):
    """ Направления работы. """
    context = {}
    context.update(get_personal_data_from_db())
    return render(request, 'home/work_directions.html', context)

def cooperation(request):
    """ Сотрудничество. """
    context = {}
    context.update(get_personal_data_from_db())
    return render(request, 'home/coopetation.html', context)

def contacts(request):
    """ Контакты. """
    context = {}
    context.update(get_personal_data_from_db())
    return render(request, 'home/contacts.html', context)