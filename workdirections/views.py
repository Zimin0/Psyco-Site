from django.shortcuts import render
from django.http import Http404

def one_direction(request, template_slug):
    """ Отдельные страницы направлений.  """
    context = {}
    directions = {
        'slug1': '...',
        'slug2': '...',
    }
    page_template = directions.get(template_slug, None)
    if not page_template:
        raise  Http404("Такого направления нет!")
    return render(request, 'workdirections/one_directions.html', context)

def directions(request):
    """ Страница всех направлений. """
    context = {}
    return render(request, 'workdirections/work_directions.html', context)