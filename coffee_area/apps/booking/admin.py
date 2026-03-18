from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'time', 'guests', 'status', 'created_at']
    list_filter = ['status', 'date']
    search_fields = ['name', 'phone', 'email']
    list_editable = ['status']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Контактные данные', {
            'fields': ('name', 'phone', 'email')
        }),
        ('Детали бронирования', {
            'fields': ('date', 'time', 'guests', 'comment')
        }),
        ('Статус', {
            'fields': ('status', 'created_at')
        }),
    )