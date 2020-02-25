from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class Chatroom(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    posted = models.DateField(default=datetime.date.today)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name='chat')
    users = models.ManyToManyField(User, related_name = 'chatrooms')

    def __str__(self):
        return(self.name)

    def get_absolute_url(self):
        return reverse('chat:index')


class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    chat = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    created_date = models.DateField(default=datetime.date.today)

    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('chat:detail', args = (self.chat_id,))

