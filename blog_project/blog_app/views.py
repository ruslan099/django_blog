from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login

from .models import *
from .forms import *
from .utils import *


class PostIndex(DataMixin, ListView):
    model = Post
    template_name = 'blog_app/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return context|c_def

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-time_create')
        

class PostCategory(DataMixin, ListView):
    model = Post
    template_name = 'blog_app/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория' + str(context['posts'][0].cat)
        c_def = self.get_user_context(title='Категория - '  + str(context['posts'][0].cat))
        return context|c_def


def show_post(request, post_slug):
    cats = Category.objects.all()
    post = get_object_or_404(Post, slug=post_slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post     #Привязываем комментарий к выбранному посту
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'cats': cats,
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'title': post.title,
    }
    return render(request, 'blog_app/post.html', context=context)


class AddPost(LoginRequiredMixin,DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog_app/addpost.html'
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('main')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление записи')
        return context|c_def


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog_app/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context|c_def

    # Метод вызывается при успешной проверке формы регистрации
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'blog_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return context|c_def

    def get_success_url(self):
        return reverse_lazy('main') 


def logout_user(request):
    logout(request)
    return redirect('login')

def about(request):
    cats = Category.objects.all()
    return render(request, 'blog_app/about.html', {'cats': cats})
