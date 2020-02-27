from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from .forms import CommentForm, CommentUpdateForm

from .models import Chatroom, Comment



class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    model = Chatroom

class DetailView(generic.DetailView):
    template_name = 'chat/detail.html'
    model = Chatroom

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # if the chatroom exists in the list of user's chatrooms
        # self.object = chat room
        # self.request.user.chatrooms.all() returns the user's chatrooms that they are a member of
        if self.object in self.request.user.chatrooms.all():
            # import pdb; pdb.set_trace()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        return HttpResponseRedirect(reverse_lazy('chat:index'))

class CreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'chat/create.html'
    model = Chatroom
    fields = ['name', 'description']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def handle_no_permission(self):
        return redirect('login')

# @user_passes_test(lambda u: u.is_superuser)
class DeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'chat/delete.html'
    model = Chatroom
    success_url = reverse_lazy('chat/index.html')
    # def get_success_url(self):
    #     return reverse_lazy('chat:index')

def add_users(request, pk):
    room = get_object_or_404(Chatroom, pk=pk)
    room.users.add(request.user)
    room.save()

    return HttpResponseRedirect(reverse_lazy('chat:index'))

class ChatroomListView(generic.ListView):
    template_name = 'chat/my_chat.html'
    model = Chatroom
    def get_queryset(self):
        return Chatroom.objects.filter(users=self.request.user)

class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.name = self.request.user 
        form.instance.chat_id = self.kwargs['pk']
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    form_class = CommentUpdateForm
    template_name = 'chat/edit.html'
    def get_success_url(self):
        return reverse_lazy('chat:index')
    def test_func(self):
        obj = self.get_object()
        return obj.name == self.request.user
