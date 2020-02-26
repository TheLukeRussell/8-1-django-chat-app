from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'userprofile')
    country = CountryField(blank_label='(select country)')
    avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username