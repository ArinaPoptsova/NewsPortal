from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.PostListView.as_view(), name='post_list'),
    path('news/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('news/search/', views.PostSearch.as_view(), name='post_search'),
    path('news/create/', views.NewsCreateView.as_view(), name='create_news'),
    path('article/create/', views.ArticleCreateView.as_view(), name='create_article'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='update_news'),
    path('article/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='update_article'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='delete_news'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='delete_article'),
    path('<category_id>/subscribe/', views.subscribe, name='subscribe'),
]
