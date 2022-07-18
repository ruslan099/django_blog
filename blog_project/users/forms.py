import email
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-reg-input'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-reg-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-reg-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-reg-input'}))

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input-edit'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input-edit'}),
            'email': forms.TextInput(attrs={'class': 'form-input-edit'}),
        }
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) == 0:
            raise forms.ValidationError('Вы не можете оставить пустым данное поле!')
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name.lower() == 'admin' or first_name.lower() == 'админ' :
            raise forms.ValidationError('Данное имя является системным!')
        return first_name

    
class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.DateInput())
    photo = forms.FileField(label='Аватар', widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-input-edit'}),
        }