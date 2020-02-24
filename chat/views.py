from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy

from .models import Chatroom


class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    model = Chatroom

class DetailView(generic.DetailView):
    template_name = 'chat/detail.html'
    model = Chatroom

class CreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'chat/create.html'
    model = Chatroom
    fields = ['name', 'description']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def handle_no_permission(self):
        return redirect('login')

