"""
Главный файл URL-ов проекта.
Здесь мы подключаем все URL-ы из приложений.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Админка
    path("admin/", admin.site.urls),
    # Главная страница
    path("", include("apps.home.urls")),
    # Приложение меню
    path("menu/", include("apps.menu.urls")),
    # Приложение коворкинга
    path("coworking/", include("apps.coworking.urls")),
    # Приложение бронирования
    path("booking/", include("apps.booking.urls")),
    path("users/", include("apps.users.urls")),
    # URL-ы для восстановления пароля (встроенные в Django)
    path("auth/", include("django.contrib.auth.urls")),

     # ============================================
    # ВОССТАНОВЛЕНИЕ ПАРОЛЯ
    # ============================================
    
    # 1. Страница ввода email
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html',           # Шаблон формы
             subject_template_name='users/password_reset_subject.txt',  # Тема письма
             email_template_name='users/password_reset_email.html',     # Тело письма
             success_url='/password-reset/done/',                # Куда после отправки
         ),
         name='password_reset'),
    
    # 2. Страница "письмо отправлено"
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    
    # 3. Страница ввода нового пароля
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             success_url='/reset/done/'
         ),
         name='password_reset_confirm'),
    
    # 4. Страница "пароль изменён"
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
