from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about', views.about,name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('tag/<int:tag_id>/', views.posts_by_tag, name='posts_by_tag'),
]