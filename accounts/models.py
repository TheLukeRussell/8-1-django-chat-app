from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from localflavor.us.us_states import STATE_CHOICES

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'userprofile')
    state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username