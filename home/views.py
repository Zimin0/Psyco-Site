from django.shortcuts import render

def home(request):
    """ Главная страница. """
    context = {}
    return render(request, 'home/home.html', context)

def about(request):
    """ Обо мне. """
    context = {}
    return render(request, 'home/about.html', context)

def work_directions(request):
    """ Направления работы. """
    context = {}
    return render(request, 'home/work_directions.html', context)

def cooperation(request):
    """ Сотрудничество. """
    context = {}
    return render(request, 'home/cooperation.html', context)
