from django.shortcuts import render
from .models import Index
from django.views.generic import ListView

class IndexView(ListView):
    model = Index
    template_name = 'index.html'

class About(ListView):
    model = Index
    template_name = 'about.html'

class Works(ListView):
    model = Index
    template_name = 'works.html'