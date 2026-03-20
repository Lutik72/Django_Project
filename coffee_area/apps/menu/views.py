from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MenuItem

@login_required
def menu_page(request):
    template = 'menu/menu.html'
    title = "Меню - Уютная кофейня"
    subtitle = "Вдохновение в каждой чашке"

    # Получаем все активные позиции меню
    menu_items = MenuItem.objects.filter(is_active=True)
    # Фильтруем по категориям
    coffee_items = menu_items.filter(category='coffee')
    dessert_items = menu_items.filter(category='desserts')
    author_items = menu_items.filter(category='author')

    context = {
        'title': title,
        "subtitle" : subtitle,
        'coffee_items': coffee_items,
        'dessert_items': dessert_items,
        'author_items': author_items,
    }
    return render(request, template, context)