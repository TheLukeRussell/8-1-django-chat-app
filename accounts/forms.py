from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from .models import Profile

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email',)

class CustomUserProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar', 'city', 'state',)