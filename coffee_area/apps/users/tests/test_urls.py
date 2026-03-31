from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class StaticURLTests(TestCase):
    def setUp(self):
        # Создаём клиент (имитация браузера) для неавторизованных запросов
        self.guest_client = Client()
        # Создаём тестового пользователя в базе данных (не авторизован, просто запись)
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        # Создаём клиент, который будет авторизован (залогинен)
        self.authorized_client = Client()
        self.authorized_client.login(username="testuser", password="testpass123")

    def test_homepage(self):
        """Главная страница доступна любому пользователю (статус 200)"""
        response = self.guest_client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_register_url(self):
        """Страница регистрации доступна для неавторизованного пользователя"""
        response = self.guest_client.get(reverse("users:register"))
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        """Страница входа доступна для неавторизованного пользователя"""
        response = self.guest_client.get(reverse("users:login"))
        self.assertEqual(response.status_code, 200)

    def test_profile_url_redirect_for_anonymous(self):
        """Неавторизованный пользователь попадает на страницу входа при попытке открыть профиль"""
        response = self.guest_client.get(reverse("users:profile"))
        expected_url = reverse("users:login") + "?next=" + reverse("users:profile")
        self.assertRedirects(response, expected_url)

    def test_profile_url_accessible_for_authenticated(self):
        """Авторизованный пользователь видит профиль (статус 200)"""
        response = self.authorized_client.get(reverse("users:profile"))
        self.assertEqual(response.status_code, 200)

    def test_logout_url_redirects(self):
        """После выхода пользователь перенаправляется на страницу входа"""
        response = self.authorized_client.get(reverse("users:logout"))
        # Проверяем, что редирект идёт на вход (users:login)
        self.assertRedirects(response, reverse("users:login"))

    def test_change_password_url_redirect_for_anonymous(self):
        """Страница смены пароля недоступна неавторизованному → редирект на логин"""
        response = self.guest_client.get(reverse("users:change_password"))
        expected_url = reverse("users:login") + "?next=" + reverse("users:change_password")
        self.assertRedirects(response, expected_url)

    def test_all_users_urls_for_authenticated_user(self):
        """Авторизованный пользователь:
        - при попытке зайти на /register/ или /login/ перенаправляется на профиль (редирект)
        - остальные страницы (профиль, смена пароля) открываются (статус 200)
        - logout перенаправляет на вход
        """
        urls_and_expected = [
            (reverse('users:register'), 'redirect_to_profile'),
            (reverse('users:login'), 'redirect_to_profile'),
            (reverse('users:profile'), 200),
            (reverse('users:change_password'), 200),
            (reverse('users:logout'), 'redirect_to_home'),
        ]
        for url, expected in urls_and_expected:
            response = self.authorized_client.get(url)
            if expected == 'redirect_to_profile':
                # Ожидаем редирект на профиль (или на главную, зависит от логики)
                # Обычно если пользователь уже залогинен, его кидает на профиль
                self.assertRedirects(response, reverse('users:profile'))
            elif expected == 'redirect_to_home':
                self.assertRedirects(response, reverse('users:login'))
            else:
                self.assertEqual(response.status_code, expected)

    def test_menu_page_redirects_anonymous(self):
        """Неавторизованный не может зайти в меню → редирект на логин"""
        response = self.guest_client.get(reverse('menu:menu'))
        expected_url = reverse('users:login') + '?next=' + reverse('menu:menu')
        self.assertRedirects(response, expected_url)

    def test_coworking_page_redirects_anonymous(self):
        """Неавторизованный не может зайти в коворкинг → редирект на логин"""
        response = self.guest_client.get(reverse('coworking:coworking'))
        expected_url = reverse('users:login') + '?next=' + reverse('coworking:coworking')
        self.assertRedirects(response, expected_url)

    def test_booking_page_redirects_anonymous(self):
        """Неавторизованный не может зайти в бронирование → редирект на логин"""
        response = self.guest_client.get(reverse('booking:booking'))
        expected_url = reverse('users:login') + '?next=' + reverse('booking:booking')
        self.assertRedirects(response, expected_url)