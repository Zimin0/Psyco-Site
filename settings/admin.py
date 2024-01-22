from django.contrib import admin
from settings.models import Setting

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
