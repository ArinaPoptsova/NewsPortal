import datetime

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author, UserCategory, Category, PostCategory
from .filters import PostFilter
from .forms import PostForm
from .exceptions import AuthorDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ObjectDoesNotExist


def subscribe(request, category_id):
    try:
        UserCategory.objects.get(category_id=category_id, subscriber=request.user)
    except UserCategory.DoesNotExist:
        usercategory = UserCategory.objects.create(category_id=category_id, subscriber=request.user)
        usercategory.save()
    return redirect('/news/')


class PostListView(ListView):
    queryset = Post.objects.order_by('-date')
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post


class PostSearch(ListView):
    queryset = Post.objects.order_by('-date')
    template_name = 'news/post_search.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        # self.filterset.
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreateView(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/edit_news.html'
    permission_required = ['add_post']

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_type = 'news'
        news.rating = 0
        if self.request.user.username in Author.objects.all().values_list('user__username', flat=True):
            news.author = Author.objects.get(user=self.request.user)
        else:
            raise AuthorDoesNotExist
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     news = self.request.POST
    #     html_content = render_to_string(
    #         'message.html',
    #         {
    #             'news': news,
    #         }
    #     )
    #     categories = [Category.objects.get(id=id) for id in map(int, news.getlist('category'))]
    #     msg = EmailMultiAlternatives(
    #         subject=news['title'],
    #         body=news['text'],
    #         from_email='lolkovalolka@yandex.ru',
    #         to=[subscriber.email for cat in categories for subscriber in cat.subscribers.all()]
    #     )
    #     msg.attach_alternative(html_content, 'text/html')
    #     msg.send()
    #     return super().post(request, *args, **kwargs)


class ArticleCreateView(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/edit_article.html'
    permission_required = ['add_post']

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_type = 'article'
        news.rating = 0
        if self.request.user.username in Author.objects.all().values_list('user__username', flat=True):
            news.author = Author.objects.get(user=self.request.user)
        else:
            raise AuthorDoesNotExist
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     news = self.request.POST
    #     html_content = render_to_string(
    #         'message.html',
    #         {
    #             'news': news,
    #         }
    #     )
    #     categories = [Category.objects.get(id=id) for id in map(int, news.getlist('category'))]
    #     msg = EmailMultiAlternatives(
    #         subject=news['title'],
    #         body=news['text'],
    #         from_email='lolkovalolka@yandex.ru',
    #         to=[subscriber.email for cat in categories for subscriber in cat.subscribers.all()]
    #     )
    #     msg.attach_alternative(html_content, 'text/html')
    #     msg.send()
    #     return super().post(request, *args, **kwargs)


class NewsUpdateView(UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/edit_news.html'
    permission_required = ['change_post']

    def test_func(self):
        obj = self.get_object()
        return obj.author.user == self.request.user


class ArticleUpdateView(UserPassesTestMixin, PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/edit_article.html'
    permission_required = ['change_post']

    def test_func(self):
        obj = self.get_object()
        return obj.author.user == self.request.user


class NewsDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author.user == self.request.user


class ArticleDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author.user == self.request.user
