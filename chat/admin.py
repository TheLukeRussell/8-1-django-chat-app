from django.contrib import admin
from .models import Chatroom, User, Comment

admin.site.register(Chatroom)
admin.site.register(Comment)