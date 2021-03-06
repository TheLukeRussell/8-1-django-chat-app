# Generated by Django 3.0.3 on 2020-02-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_auto_20200224_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='title',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(related_name='chatroom', to='chat.User'),
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='name',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='name',
            field=models.CharField(default='use string', max_length=255),
            preserve_default=False,
        ),
    ]
