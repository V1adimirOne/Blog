"""Определяет схемы url для пользователей"""
from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
	# Включить url для авторизации по умолчанию
	path('', include('django.contrib.auth.urls')),
	# Страница регистрации
	path('register/', views.register, name='register'),
]