from django.db import models
from django.urls import reverse

class Chat(models.Model):
    name = models.CharField(max_length = 255)
    comments = models.ManyToManyField('Comment', related_name = 'chat')

    def __str__(self):
        return(self.name)

    def get_absolute_url(self):
        return reverse('chat:index')
    
class Comment(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.name
    