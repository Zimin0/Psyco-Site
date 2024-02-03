from django.shortcuts import render, get_object_or_404

from services.models import Service
from settings.upload_info import get_personal_data_from_db


def services(request):
    """ Услуги и цены """
    context = {
        'services': Service.objects.filter()
    }
    context.update(get_personal_data_from_db())
    return render(request, 'services/services.html', context)


def service(request, id):
    """ Услуги и цены """
    context = {
        'service': get_object_or_404(Service, id=id)
    }
    context.update(get_personal_data_from_db())
    return render(request, 'services/service1.html', context)
