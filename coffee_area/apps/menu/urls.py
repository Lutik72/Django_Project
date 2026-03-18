from django.urls import path
from . import views
from django.contrib import admin

# app_name для обратного резолвинга URL-ов
app_name = 'menu'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu_page, name='menu'),
]