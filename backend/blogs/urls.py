from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog-list'),
    path('crawl/<str:tag_name>/', views.crawl_tag, name='crawl-tag'),
]

