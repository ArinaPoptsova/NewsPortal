from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.order_by('-date')


class PostDetailView(DetailView):
    model = Post
