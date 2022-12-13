
import django_filters
from django.db import models
from django_filters.widgets import RangeWidget

from .models import Post, Category
from django import forms


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter()
    date = django_filters.DateTimeFilter(widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = ['title', 'category', 'date']

