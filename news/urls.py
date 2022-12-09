from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.PostListView.as_view()),
    path('news/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]
