from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Chatroom


class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    model = Chatroom

class DetailView(generic.DetailView):
    template_name = 'chat/detail.html'
    model = Chatroom