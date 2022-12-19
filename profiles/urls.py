from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/create/', views.CreateProfileView.as_view(), name='create_profile'),
    path('<int:pk>/update/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('upgrade/', views.upgrade_me, name='upgrade'),
]
