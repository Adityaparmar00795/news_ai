from . import views 
from django.urls import path

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('create/', views.news_create, name='news_create'),
    path('<int:news_id>/edit/', views.news_edit, name='news_edit'),
    path('<int:news_id>/delete/', views.news_delete, name='news_delete'),
       path('register/', views.register, name='register'),
       path("google-news/", views.google_news, name="google_news"),
       path("article/", views.article_view, name="article_view"),
       path("summarize/", views.summarize_news, name="summarize_news"),
       path("ask-ai/", views.ask_ai, name="ask_ai"),
]
