from django.urls import path
from . import views
from django.contrib import admin

# app_name для обратного резолвинга URL-ов
app_name = 'coworking'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.coworking_page, name="coworking")
]