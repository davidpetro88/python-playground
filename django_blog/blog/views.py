from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category, Post


def home(request):
    name = "David"
    posts = Post.objects.filter(status='Published')
    all_categories = Category.objects.all()
    context = {
        'name': name,
        'categories': all_categories,
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def show_posts_by_category(request, category_id):
    all_categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    posts = Post.objects.filter(category=category, status='Published')
    context = {
        'posts': posts,
        'categories': all_categories,
        'category': category
    }
    return render(request, 'blog/home.html', context)