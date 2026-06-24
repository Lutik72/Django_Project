from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_page, name='booking'),
    path('my-bookings/', views.my_bookings_view, name='my_bookings'),  # ← ЭТА СТРОКА ДОЛЖНА БЫТЬ
]