from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Tariff(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название тарифа",
        help_text="Например: Час, День, Абонемент"
    )
    price = models.IntegerField(
        verbose_name="Цена (в рублях)",
        validators=[MinValueValidator(0)]
    )
    description = models.CharField(
        max_length=200,
        verbose_name="Описание",
        help_text="Краткое описание тарифа"
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Порядок сортировки",
        help_text="Чем меньше число, тем выше карточка"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активно",
        help_text="Отображать ли тариф на сайте"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
        ordering = ['order', 'id']  # Сортировка по порядку, затем по id

    def __str__(self):
        return f"{self.name} - {self.price} ₽"

    def formatted_price(self):
        """Возвращает цену с пробелом для тысяч (если понадобится)"""
        return f"{self.price:,}".replace(",", " ")