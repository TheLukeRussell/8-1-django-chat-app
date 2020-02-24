from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Chat, Comment

class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    model = Chat