from django.urls import path
from . import views
app_name = 'blogapp'

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/update/<int:pk>/', views.post_update, name='post_update'),
    path('posts/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('front-posts/', views.front_post_view, name='front_posts'),
  
]