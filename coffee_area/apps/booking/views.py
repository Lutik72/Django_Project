from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking  # ← ДОБАВЬ ЭТУ СТРОКУ
import random

@login_required
def booking_page(request):
    """Страница бронирования"""

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

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            
            messages.success(request, "Спасибо! Ваша заявка принята.")
            return redirect("booking:my_bookings")
    else:
        form = BookingForm()
    
    context = {
        "form": form,
        "title": "Бронирование места в коворкинге",
        "subtitle": random_quote,
    }
    
    return render(request, "booking/booking.html", context)


@login_required
def my_bookings_view(request):
    """История бронирований пользователя"""
    
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'bookings': bookings,
        'total_bookings': bookings.count(),
        'title': 'Мои бронирования',
    }
    
    return render(request, 'booking/my_bookings.html', context)