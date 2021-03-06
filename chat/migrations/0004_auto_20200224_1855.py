# Generated by Django 3.0.3 on 2020-02-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.AddField(
            model_name='comment',
            name='comments',
            field=models.ManyToManyField(related_name='chat', to='chat.Comment'),
        ),
    ]
