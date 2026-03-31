from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import RegisterForm, LoginForm
import random


def register_view(request):
    """Регистрация пользователя"""

    if request.user.is_authenticated:
        return redirect("users:profile")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно! Добро пожаловать!")
            return redirect("users:profile")
        else:
            messages.error(request, "Ошибка регистрации. Проверьте введенные данные.")
    else:
        form = RegisterForm()

    context = {
        "form": form,
        "title": "Регистрация",
    }

    return render(request, "users/register.html", context)


def login_view(request):
    """Вход пользователя"""

    if request.user.is_authenticated:
        return redirect("users:profile")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Добро пожаловать, {username}!")
                return redirect("users:profile")
            else:
                messages.error(request, "Неверное имя пользователя или пароль.")
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    else:
        form = LoginForm()

    context = {"form": form, "title": "Вход"}
    return render(request, "users/login.html", context)


def logout_view(request):
    """Выход из аккаунта"""

    logout(request)
    messages.info(request, "Вы вышли из аккаунта.")
    return redirect("users:login")

@login_required
def profile_view(request):
    """Личный кабинет"""

    subtitle = [
        "Добро пожаловать туда, где пахнет счастьем и корицей.",
        "Кофе — это маленькое удовольствие в большой чашке.",
        "Наша кофейня — место, где время останавливается, чтобы насладиться моментом.",
        "Кофе решает всё. Особенно утром.",
        "Хороший день начинается с ароматного кофе и уютной атмосферы.",
        "Мечты сбываются у тех, кто пьёт кофе и верит в чудеса.",
        "В каждой чашке нашего кофе — частичка души и тепло обжаренных зёрен.",
        "Кофе — это не просто напиток, это философия медленной жизни.",
        "Живи, люби, пей кофе.",
        "У нас вы найдёте не только отличный кофе, но и вдохновение.",
        "Секрет хорошего кофе прост: любовь к своему делу и лучшие зёрна.",
        "Жизнь слишком коротка, чтобы пить плохой кофе.",
        "Кофейня — это островок уюта в шумном городе.",
        "Хороший кофе согревает не только руки, но и душу.",
        "Каждая чашка кофе — это новая страница твоего дня. Напиши её красиво.",
        "Каждая чашка кофе уникальна, как и наши гости.",
        "Мы верим, что настоящий кофе сближает людей.",
    ]
    random_quote = random.choice(subtitle)

    context = {
        "user": request.user,
        "title": f"Личный кабинет - {request.user.username}",
        "subtitle": random_quote,
    }
    return render(request, "users/profile.html", context)

@login_required
def change_password_view(request):
    """Смена пароля"""

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Обновляем сессию, чтобы пользователь не вышел после смены пароля
            update_session_auth_hash(request, user)
            messages.success(request, "Пароль успешно изменен!")
            return redirect("users:profile")
        else:
            messages.error(request, "Ошибка. Проверьте правильность ввода.")
    else:
        form = PasswordChangeForm(request.user)

    context = {
        "form": form,
        "title": "Смена пароля",
    }
    return render(request, "users/change_password.html", context)
