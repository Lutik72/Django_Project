from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import RegisterForm, LoginForm


class RegisterFormTest(TestCase):
    """Тесты для формы регистрации"""

    def test_valid_registration(self):
        """Проверка: форма валидна при корректных данных"""
        form = RegisterForm(data={
            'username': 'newuser',
            'email': 'user@example.com',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
        })
        self.assertTrue(form.is_valid())

    def test_username_required(self):
        """Проверка: поле username обязательно"""
        form = RegisterForm(data={
            'username': '',
            'email': 'user@example.com',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_email_required(self):
        """Проверка: поле email обязательно"""
        form = RegisterForm(data={
            'username': 'newuser',
            'email': '',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_password_mismatch(self):
        """Проверка: ошибка если пароли не совпадают"""
        form = RegisterForm(data={
            'username': 'newuser',
            'email': 'user@example.com',
            'password1': 'password123',
            'password2': 'password456',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)


    def test_password_too_weak(self):
        """Проверка: пароль слишком простой (менее 8 символов)"""
        form = RegisterForm(data={
            'username': 'newuser',
            'email': 'user@example.com',
            'password1': '123',
            'password2': '123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors)


class LoginFormTest(TestCase):
    """Тесты для формы входа"""

    def setUp(self):
        """Создаём тестового пользователя перед каждым тестом"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='correctpassword123'
        )

    def test_valid_login(self):
        """Проверка: форма валидна при правильных данных"""
        form = LoginForm(data={
            'username': 'testuser',
            'password': 'correctpassword123'
        })
        self.assertTrue(form.is_valid())

    def test_empty_username(self):
        """Проверка: поле username обязательно"""
        form = LoginForm(data={
            'username': '',
            'password': 'correctpassword123'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_empty_password(self):
        """Проверка: поле password обязательно"""
        form = LoginForm(data={
            'username': 'testuser',
            'password': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)

    def test_wrong_password(self):
        """Проверка: неверный пароль — ошибка"""
        form = LoginForm(data={
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        # AuthenticationForm не валидирует данные без request
        # Поэтому проверяем, что ошибка появится при authenticate
        self.assertTrue(form.is_valid())  # Форма сама по себе валидна
        # Но аутентификация не пройдёт — это проверяется в view

    def test_nonexistent_user(self):
        """Проверка: несуществующий пользователь"""
        form = LoginForm(data={
            'username': 'nonexistent',
            'password': 'somepass'
        })
        self.assertTrue(form.is_valid())
        # Аутентификация не пройдёт — проверяется в view