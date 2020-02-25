from django import forms
from .models import Chatroom, Comment
from crispy_forms.helper import FormHelper
from parsley.decorators import parsleyfy

@parsleyfy
class CommentForm(forms.ModelForm):

    class Meta:
        fields = ('comment',)
        model = Comment


    