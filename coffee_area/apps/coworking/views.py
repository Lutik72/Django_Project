# from .models import Tariff
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required 
def coworking_page(request):
    template = "coworking/coworking.html"
    title = "Уютная кофейня"
    subtitle = "Коворкинг с ароматом кофе — твой второй офис в сердце города"
    # tariffs = Tariff.objects.filter(is_active=True).order_by('order')
  
    context = {
        "title": title,
        "subtitle": subtitle,
        # 'tariffs': tariffs,
    }
    return render(request, template, context)