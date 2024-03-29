from django.contrib.auth.forms import AuthenticationForm
from django import forms

class UserLoginForm (AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs = {
        'class': 'form-control py-4',
        'placeholder':'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs = {
        'class': 'form-control py-4',
        'placeholder':'Введите пароль'
    }))
    
    class Meta:
        model = 'User'
        fields = ('username', 'password')
        pass