from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class AddPostForm(forms.ModelForm):
    error_css_class = "flash-error"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не указана"

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'photo','is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input-comm'}),
            'slug': forms.TextInput(attrs={'class': 'form-input-comm'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea form-textarea-big'}),
        }
    
    # Создание пользовательских валидаторов
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise forms.ValidationError('Оу, длина превышает 200 символов!')
        return title


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-input-comm'}))
    email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-input-comm'}))
    body = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={'class': 'form-textarea'}))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Ваш логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))