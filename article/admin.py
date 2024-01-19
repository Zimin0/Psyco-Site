from django.contrib import admin

from article.models import Article

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_display = ['id', 'title']