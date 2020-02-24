from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class Chatroom(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    posted = models.DateField(default=datetime.date.today)
    users = models.ManyToManyField('User', related_name = 'chatroom')
    comments = models.ManyToManyField('Comment', related_name = 'chatroom')

    def __str__(self):
        return(self.name)

    def get_absolute_url(self):
        return reverse('chat:index')

class User(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__(self):
        return(self.name)

class Comment(models.Model):
    comment = models.TextField()