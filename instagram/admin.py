from django.contrib import admin

from instagram.models import Hashtag, Post, Comment

admin.site.register(Hashtag)
admin.site.register(Post)
admin.site.register(Comment)
