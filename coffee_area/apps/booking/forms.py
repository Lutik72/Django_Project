from django import forms
from .models import Booking
from apps.coworking.models import Tariff
from datetime import date, time

class BookingForm(forms.ModelForm):
    """Форма для бронирования"""
    
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'email', 'guests', 'date', 'time', 'tariff', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input', 'id': 'id_date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input', 'id': 'id_time'}),
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваше имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+7 (999) 123-45-67'}),
            'guests': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 20}),
            'tariff': forms.Select(attrs={'class': 'form-input', 'id': 'id_tariff'}),  # Выпадающий список
            'comment': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Особые пожелания...'}),
        }
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'email': 'Email',
            'guests': 'Количество гостей',
            'date': 'Дата',
            'time': 'Время',
            'tariff': 'Тариф',
            'comment': 'Комментарий',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Загружаем тарифы из БД (только активные)
        self.fields['tariff'].queryset = Tariff.objects.filter(is_active=True) if hasattr(Tariff, 'is_active') else Tariff.objects.all()
        self.fields['tariff'].empty_label = 'Выберите тариф'
    
    def clean_date(self):
        selected_date = self.cleaned_data['date']
        if selected_date < date.today():
            raise forms.ValidationError('Дата не может быть в прошлом')
        return selected_date
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) < 10:
            raise forms.ValidationError('Введите корректный номер телефона')
        return phone