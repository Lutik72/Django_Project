from django.http import HttpResponse

# пока страница ещё в разработке
def booking_development(request):
    """Страница бронирования в разработке"""
    html = """
    <h1>🚧 Страница в разработке</h1>
    <p>Раздел бронирования скоро появится!</p>
    <p><a href="/">Вернуться на главную</a></p>
    <p><a href="/coworking/">Вернуться в коворкинг</a></p>
    """
    return HttpResponse(html)