from django.shortcuts import render, get_object_or_404
from .models import blog
from . import views as blog_views
from django.urls import path

urlpatterns = [
	path('', blog_views.bloghome, name='bloghome'),
	path('<str:url>/', blog_views.blogdetail.as_view(), name='blog-detailed'),
    path('category/<str:categories>/', blog_views.blogcategory.as_view(), name='blog-categories'),
]