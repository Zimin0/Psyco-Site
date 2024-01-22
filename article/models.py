from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=40, verbose_name="Заголовок статьи", help_text='Отображается на главной страницe.')
    pre_text = models.CharField(max_length=170, verbose_name="Краткий текст-превью", help_text='Отображается на главной страницe.')
    pre_image = models.ImageField(verbose_name="Картинка-превью", help_text='Отображается на главной страницe.')
    text = RichTextField(verbose_name="Основной текст статьи")