from django.shortcuts import render, get_object_or_404

from article.models import Article
from settings.upload_info import get_personal_data_from_db

def article(request, id):
    """ Статья. """
    context = {}
    context.update(get_personal_data_from_db())
    article = get_object_or_404(Article, id=id)
    context['article'] = article
    return render(request, 'article/article.html', context)