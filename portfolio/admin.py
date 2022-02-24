from django.contrib import admin
from .models import Post, Index, Comment, Like, View

admin.site.site_header = "Zaman's Portfolio "
admin.site.site_title = "Zaman"
admin.site.index_title = "Admin"

admin.site.register(Post)
admin.site.register(Index)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(View)