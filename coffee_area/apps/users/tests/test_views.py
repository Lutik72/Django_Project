from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UsersViewsTemplateTests(TestCase):
    def setUp(self):
        # Клиент для запросов
        self.client = Client()
        # Создаём тестового пользователя (но не логиним его)
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_register_view_uses_correct_template(self):
        """Регистрация использует шаблон users/register.html"""
        response = self.client.get(reverse('users:register'))
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login_view_uses_correct_template(self):
        """Вход использует шаблон users/login.html"""
        response = self.client.get(reverse('users:login'))
        self.assertTemplateUsed(response, 'users/login.html')

    def test_profile_view_uses_correct_template_for_authenticated(self):
        """Профиль использует шаблон users/profile.html для авторизованного"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('users:profile'))
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_change_password_view_uses_correct_template_for_authenticated(self):
        """Смена пароля использует шаблон users/change_password.html для авторизованного"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('users:change_password'))
        self.assertTemplateUsed(response, 'users/change_password.html')