from django.shortcuts import render, get_object_or_404

from article.models import Article

def article(request, id):
    """ Статья. """
    context = {}
    article = get_object_or_404(Article, id=id)
    context['article'] = article
    return render(request, 'article/article.html', context)