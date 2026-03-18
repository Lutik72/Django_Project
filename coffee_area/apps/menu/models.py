from django.db import models

class MenuItem(models.Model):
    """Модель позиции меню"""
    
    # Категории - простой выбор
    CATEGORY_CHOICES = [
        ('coffee', 'Кофе'),
        ('desserts', 'Десерты'),
        ('author', 'Авторские напитки'),
    ]
    
    # Основные поля
    category = models.CharField(
        'Категория', 
        max_length=20, 
        choices=CATEGORY_CHOICES,
        default='coffee'
    )
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', max_length=500)
    price = models.IntegerField('Цена')  # Просто число
    
    # Дополнительные поля (можно оставить пустыми)
    ingredients = models.CharField('Ингредиенты', max_length=300, blank=True)
    badge = models.CharField('Значок', max_length=50, blank=True, null=True)
    
    # Поля для сортировки и отображения
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)
    
    def __str__(self):
        return f"{self.name} - {self.price}₽"
    
    class Meta:
        verbose_name = 'Позиция меню'
        verbose_name_plural = 'Позиции меню'
        ordering = ['category', 'order']  # Сортировка по категории и порядку