from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Post, Author, Category, PostCategory, Comment, UserCategory


@admin.register(Post)
class PostModelAdmin(ModelAdmin):
    list_display = ['title', 'author', 'date']
    list_filter = ['category', 'date', 'author__user__username', 'post_type']


@admin.register(Author)
class AuthorModelAdmin(ModelAdmin):
    list_display = ['user']


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    list_display = ['name']


@admin.register(PostCategory)
class PostCategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Comment)
class CommentModelAdmin(ModelAdmin):
    list_display = ['post', 'user', 'date']
    list_filter = ['post__title', 'user__username', 'date']


@admin.register(UserCategory)
class UserCategoryModelAdmin(ModelAdmin):
    pass
