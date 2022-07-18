import profile
from django.shortcuts import render, redirect
from django.contrib import messages
from flask_login import login_required
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from blog_app.models import *
from users.models import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)

            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        form = UserRegisterForm()
        context = {
            'form': form,
            'title': 'Регистрация'
        }
        cats = Category.objects.all()
        context['cats'] = cats

    return render(request, 'users/register.html', context=context)

# @login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Информация о профиле успешно обновлена')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'title': 'Регистрация'
        }
    cats = Category.objects.all()
    context['cats'] = cats
    return render(request, 'users/edit.html', context=context)

