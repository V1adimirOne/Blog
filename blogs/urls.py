"""Определение схемы url для приложения blogs"""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница для добавления новой записи
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:texts_id>/', views.edit_post, name='edit_post'),
]