from django.contrib import admin
from .models import Post, Index

admin.site.site_header = "Zaman's Portfolio "
admin.site.site_title = "Zaman"
admin.site.index_title = "Admin"

admin.site.register(Post)
admin.site.register(Index)
