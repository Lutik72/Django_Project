from django.urls import path, include
from . import views

# app_name для обратного резолвинга URL-ов
app_name = 'home'

urlpatterns = [
    # Главная страница
    path('', views.home_page, name='home'),
]