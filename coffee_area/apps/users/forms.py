from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class RegisterForm(UserCreationForm):
    """Форма регистрации"""
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'Email'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы для стилей
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Имя пользователя'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Повторите пароль'
        })

class LoginForm(AuthenticationForm):
    """Форма входа"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Имя пользователя'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Пароль'
        })

    class RegisterForm(UserCreationForm):
        """Форма регистрации"""
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'Email'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Имя пользователя'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Повторите пароль'
        })


class LoginForm(AuthenticationForm):
    """Форма входа"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Имя пользователя'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Пароль'
        })


class UserUpdateForm(forms.ModelForm):
    """Форма для редактирования профиля"""
    
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Имя пользователя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email'
            }),
        }
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
    
    def clean_username(self):
        """Проверка, что username уникален"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Это имя пользователя уже занято')
        return username
    
    def clean_email(self):
        """Проверка, что email уникален"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Этот email уже используется')
        return email