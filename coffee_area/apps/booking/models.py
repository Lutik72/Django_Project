from django.db import models
from django.contrib.auth.models import User
from apps.coworking.models import Tariff  # Импортируем модель Tariff

class Booking(models.Model):
    """Модель для заявок на бронирование"""
    
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('confirmed', 'Подтверждена'),
        ('cancelled', 'Отменена'),
    ]
    
    # Контактные данные
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    
    # Детали бронирования
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    guests = models.PositiveIntegerField('Количество гостей', default=1)
    
    # Связь с тарифом (НОВОЕ ПОЛЕ)
    tariff = models.ForeignKey(
        Tariff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Тариф'
    )
    
    # Дополнительная информация
    comment = models.TextField('Комментарий', blank=True)
    
    # Служебные поля
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    # Связь с пользователем
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
    
    class Meta:
        verbose_name = 'Заявка на бронирование'
        verbose_name_plural = 'Заявки на бронирование'
        ordering = ['-created_at']