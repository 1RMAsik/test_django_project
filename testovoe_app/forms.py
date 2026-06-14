from django import forms
from .models import Request

class RequestCreateForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['client_name', 'phone', 'email', 'subject', 'message']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван Иванов'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 123-45-67'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема обращения'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Опишите вашу проблему...'}),
        }