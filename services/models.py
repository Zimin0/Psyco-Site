from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название услуги" )
    pre_text = models.CharField(max_length=200, verbose_name="Краткий текст-превью")
    price = models.IntegerField(default=0, verbose_name="Цена")

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        new_title = " ".join(self.title.split()[:10]) + '...'
        return f'{new_title}'