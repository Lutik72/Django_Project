from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    list_editable = ['order', 'is_active']  # Можно редактировать прямо в списке
    search_fields = ['name', 'description']
    
    fieldsets = (
        ('Основное', {
            'fields': ('category', 'name', 'description', 'price')
        }),
        ('Дополнительно', {
            'fields': ('ingredients', 'badge'),
            'classes': ('collapse',)  # Скрыто по умолчанию
        }),
        ('Настройки отображения', {
            'fields': ('order', 'is_active')
        }),
    )