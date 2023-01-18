from django.contrib import admin

from dscrapy.news.models import Article


@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    pass
