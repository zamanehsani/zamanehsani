from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Index(models.Model):
    first_name         = models.CharField(max_length=150, null=True, blank=True)
    last_name          = models.CharField(max_length=150, null=True, blank=True)
    position           = models.CharField(max_length=150, null=True, blank=True)
    company            = models.CharField(max_length=150, null=True, blank=True)
    email         = models.EmailField(null=True, blank=True)
    message      = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField (max_length= 500)
    date = models.DateField(default=timezone.now)
    post = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(default= 'Post_cover.jpg', upload_to='blog_pics')
    views = models.IntegerField(default=0)

    def __str__(self):
        
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.SmallIntegerField()

class View(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    view = models.IntegerField()
