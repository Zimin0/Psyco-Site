from django.shortcuts import render
from settings.upload_info import get_personal_data_from_db

def one_direction(request, index):
    """ Отдельные страницы направлений.  """
    context = {}
    context.update(get_personal_data_from_db())
    return render(request, f'workdirections/direction{index}.html', context)