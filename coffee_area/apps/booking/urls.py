from django.urls import path
from . import views

# app_name для обратного резолвинга URL-ов
app_name = 'booking'

urlpatterns = [
    # В разработке
    path('', views.booking_development, name='booking'),
    # подключить когда будет готово
    # path('', views.booking_page, name='booking'),
]