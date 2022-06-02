from django.urls import path
from .views import *

urlpatterns = [
    path('', PostIndex.as_view(), name='main'),
    path('about/', about, name='about'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
    path('post/<slug:post_slug>', show_post, name='showpost'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
