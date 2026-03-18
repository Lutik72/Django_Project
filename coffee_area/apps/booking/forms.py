from django import forms
from .models import Booking
from datetime import date, time

class BookingForm(forms.ModelForm):
    """Форма для бронирования"""
    
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'email', 'date', 'time', 'guests', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваше имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+7 (999) 123-45-67'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'example@mail.ru'}),
            'guests': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'max': 20}),
            'comment': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Особые пожелания...'}),
        }
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'email': 'Email',
            'date': 'Дата',
            'time': 'Время',
            'guests': 'Количество гостей',
            'comment': 'Комментарий',
        }
    
    def clean_date(self):
        """Проверка, что дата не в прошлом"""
        selected_date = self.cleaned_data['date']
        if selected_date < date.today():
            raise forms.ValidationError('Дата не может быть в прошлом')
        return selected_date
    
    def clean_phone(self):
        """Простая проверка телефона"""
        phone = self.cleaned_data['phone']
        # Убираем все не-цифры для проверки
        digits = ''.join(filter(str.isdigit, phone))
        if len(digits) < 10:
            raise forms.ValidationError('Введите корректный номер телефона')
        return phone