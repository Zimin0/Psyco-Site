from settings.models import Setting
from django.shortcuts import get_object_or_404

def get_personal_data_from_db() -> dict:
    """ 
    Подтягивает информацию о телефоне, почте и адресе владельца. 
    * PHONE_NUMBER
    * EMAIL
    * ADDRESS
    """
    return {
        'PHONE_NUMBER': get_object_or_404(Setting, slug='PHONE_NUMBER').value,
        'EMAIL': get_object_or_404(Setting, slug='EMAIL').value,
        'ADDRESS':get_object_or_404(Setting, slug='ADDRESS').value
    }
