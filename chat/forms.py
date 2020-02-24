from django import forms
from .models import Chatroom, Comment

from parsley.decorators import parsleyfy

@parsleyfy
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)