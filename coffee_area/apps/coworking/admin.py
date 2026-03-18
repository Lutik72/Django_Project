from django.contrib import admin
from django.db import models
from .models import Tariff

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    # Поля, отображаемые в списке тарифов
    list_display = ('name', 'price', 'description_short', 'order', 'is_active')
    
    # Поля, по которым можно фильтровать
    list_filter = ('is_active', 'created_at')
    
    # Поля, по которым можно искать
    search_fields = ('name', 'description')
    
    # Поля для редактирования прямо в списке
    list_editable = ('order', 'is_active')
    
    # Поля только для чтения
    readonly_fields = ('created_at', 'updated_at')
    
    # Разбивка на группы
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'price', 'description')
        }),
        ('Настройки отображения', {
            'fields': ('order', 'is_active')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Скрыто по умолчанию
        }),
    )
    
    def description_short(self, obj):
        """Обрезает длинное описание для списка"""
        if obj.description and len(obj.description) > 30:
            return obj.description[:30] + "..."
        return obj.description or ""
    description_short.short_description = "Описание"
    
    # Сохраняем сортировку при добавлении
    def save_model(self, request, obj, form, change):
        if not obj.order:
            # Если порядок не указан, ставим последним
            last_order = Tariff.objects.aggregate(
                models.Max('order')
            )['order__max']
            obj.order = (last_order or 0) + 10
        super().save_model(request, obj, form, change)