from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок статьи", help_text='Отображается на главной страницe.')
    pre_text = models.CharField(max_length=170, verbose_name="Краткий текст-превью", help_text='Отображается на главной страницe.')
    pre_image = models.ImageField(verbose_name="Картинка-превью", help_text='Отображается на главной страницe.')
    text = RichTextField(verbose_name="Основной текст статьи")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.get_cropped_title()
    
    def get_cropped_title(self):
        new_title = " ".join(self.title.split()[:5]) + '...'
        return f'{new_title}'