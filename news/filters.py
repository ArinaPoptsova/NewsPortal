
import django_filters
from django.db import models
from django_filters.widgets import RangeWidget

from .models import Post, Category
from django import forms


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter()
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all().values_list('name', flat=True))
    date = django_filters.DateTimeFilter(widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = ['title', 'category', 'date']
        filter_overrides = {
            models.DateTimeField: {
                'filter_class': django_filters.DateTimeFilter,
                'extra': lambda f: {
                    'widget': forms.DateTimeInput,
                },

            },
            models.CharField: {
                'filter_class': django_filters.DateTimeFilter,
                'extra': lambda f: {
                    'widget': forms.Select,
                },

            }
        }
