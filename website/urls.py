"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from portfolio import views as zee_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', zee_view.IndexView.as_view(), name="home_page"),
    path('about', zee_view.About.as_view(), name='about'),
    path('work', zee_view.Works.as_view(), name='works'),
    path('service', zee_view.Service.as_view(), name='service'),
    path('blog', zee_view.Blog.as_view(), name='blog'),
    path('contact', zee_view.Contact.as_view(), name='contact'),
    path("post/<int:pk>", zee_view.Post.as_view(), name="post"),
    # path("add_comment", zee_view.Post.add_comment, name="add_comment"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)