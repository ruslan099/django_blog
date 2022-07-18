from django.contrib import admin
from django.urls import path, include
from .views import *
 
urlpatterns = [
	path('register/', register, name='register'),
	path('edit/', edit, name='edit'),
]