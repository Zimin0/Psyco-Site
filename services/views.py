from django.shortcuts import render


def services(request):
    """ Услуги и цены """
    context = {}
    return render(request, 'services/services.html', context)
