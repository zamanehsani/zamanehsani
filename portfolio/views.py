from gc import get_objects
from pyexpat import model
from django.shortcuts import render, HttpResponse, redirect

from portfolio import forms
from .models import Index, Post, Comment, View
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

    def get_context_data(self, **kwargs):
        context = super(Post, self).get_context_data(**kwargs)
        # get post object and increment the view in each get request
        obj = self.get_object()
        views = obj.views
        views +=1
        obj.views = views
        obj.save()
        return context


    def post(self, request, pk):
        from . import forms
        from django.core.mail import send_mail
        from django.conf import settings
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save()

            # sending a welcoming email
            # message = " your have recieved a comment on your post\n"
            # message += "\""
            # message +=  form.cleaned_data.get('comment')
            # message += "\""
            # name = form.cleaned_data.get('name')
            # send_mail(
            #      name + ' has commented on your post',
            #     message,
            #     settings.EMAIL_HOST_USER,
            #     ['zamanehsani@yahoo.com'],
            #     fail_silently=False,
            # )
            return redirect('post', request.POST.get('post'))

    # def add_comment(request):
    #     if request.mothod == 'POST':
    #         name = request.POST['name']
    #         email = request.POST['email']
    #         comment = request.POST['comment']

    #         Comment.objects.create(
    #             name = name,
    #             email = email,
    #             comment = comment
    #         )

            # return HttpResponse('')

class Contact(ListView):
    model = Index
    template_name = 'contact.html'
