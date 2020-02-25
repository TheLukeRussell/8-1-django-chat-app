from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from .forms import CommentForm

from .models import Chatroom, Comment


class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    model = Chatroom

class DetailView(generic.DetailView):
    template_name = 'chat/detail.html'
    model = Chatroom
    def get_queryset(self):
        return Chatroom.objects.filter(users=self.request.user)

class CreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'chat/create.html'
    model = Chatroom
    fields = ['name', 'description']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def handle_no_permission(self):
        return redirect('login')

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'chat/delete.html'
    model = Chatroom
    success_url = reverse_lazy('chat/index.html')
    def get_success_url(self):
        return reverse_lazy('chat:index')

class JoinView(LoginRequiredMixin, generic.UpdateView):
    model = Chatroom
    fields = ['users',]

class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.name = self.request.user 
        form.instance.chat_id = self.kwargs['pk']
        return super().form_valid(form)