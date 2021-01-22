from django.shortcuts import render
from .models import Index, Post
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    model = Index
    template_name = 'index.html'

class About(ListView):
    model = Index
    template_name = 'about.html'

class Works(ListView):
    model = Index
    template_name = 'works.html'

class Service(ListView):
    model = Index
    template_name = 'services.html'

class Blog(ListView):
    model = Post
    context_object_name = 'objects'
    template_name = 'blog.html'
    ordering = ['-date']
    paginate_by = 3

class Post(DetailView):
    model = Post
    template_name = 'post.html'


class Contact(ListView):
    model = Index
    template_name = 'contact.html'