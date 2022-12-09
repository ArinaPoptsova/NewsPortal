from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Post, Author


@admin.register(Post)
class PostModelAdmin(ModelAdmin):
    pass


@admin.register(Author)
class AuthorModelAdmin(ModelAdmin):
    pass
