from django.urls import path
from . import views
from django.contrib import admin

# app_name для обратного резолвинга URL-ов
app_name = 'booking'

urlpatterns = [
    path('admin/', admin.site.urls),
    # В разработке
    # path('', views.booking_development, name='booking'),
    # подключить когда будет готово
    path('', views.booking_page, name='booking'),
]