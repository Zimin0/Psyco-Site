from django.shortcuts import render

from services.models import Service


def services(request):
    """ Услуги и цены """
    context = {
        'services': Service.objects.filter()
    }
    return render(request, 'services/services.html', context)
