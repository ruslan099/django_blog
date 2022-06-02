from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    
    # Создание пользовательских валидаторов
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise forms.ValidationError('Оу, длина превышает 200 символов!')
        return title


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-input'}))
    body = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={'class': 'form-input'}))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-reg-input'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-reg-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-reg-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-reg-input'}))

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Ваш логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))