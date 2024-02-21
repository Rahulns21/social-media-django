from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('create', views.create_post, name='create-post'),
    path('feed', views.feed, name='feed'),
    path('like', views.like_post, name='like'),
]
