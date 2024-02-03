from django.shortcuts import render

from services.models import Service
from settings.upload_info import get_personal_data_from_db


def services(request):
    """ Услуги и цены """
    context = {
        'services': Service.objects.filter()
    }
    context.update(get_personal_data_from_db())
    return render(request, 'services/services.html', context)
