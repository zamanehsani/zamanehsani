from django.shortcuts import render, HttpResponse
from .models import Index, Post, Comment, Like
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

    def add_comment(request):
        if request.mothod == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            comment = request.POST['comment']

            Comment.objects.create(
                name = name,
                email = email,
                comment = comment
            )

            return HttpResponse('')

class Contact(ListView):
    model = Index
    template_name = 'contact.html'