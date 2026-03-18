"""
Главный файл URL-ов проекта.
Здесь мы подключаем все URL-ы из приложений.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    
    # Главная страница
    path('', include('apps.home.urls')),
    
    # Приложение меню
    path('menu/', include('apps.menu.urls')),
    
    # Приложение коворкинга
    path('coworking/', include('apps.coworking.urls')),
    
    # Приложение бронирования
    path('booking/', include('apps.booking.urls')),
]