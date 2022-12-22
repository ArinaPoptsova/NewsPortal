from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Post, Author, Category, PostCategory, Comment, UserCategory


@admin.register(Post)
class PostModelAdmin(ModelAdmin):
    pass


@admin.register(Author)
class AuthorModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(PostCategory)
class PostCategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Comment)
class CommentModelAdmin(ModelAdmin):
    pass


@admin.register(UserCategory)
class UserCategoryModelAdmin(ModelAdmin):
    pass
