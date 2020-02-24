# Generated by Django 3.0.3 on 2020-02-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_auto_20200224_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='users',
        ),
        migrations.RemoveField(
            model_name='group_name',
            name='owner',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='title',
            field=models.CharField(default='use string', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group_name',
            name='name',
            field=models.CharField(default='use string', max_length=255),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='name',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='name',
            field=models.ManyToManyField(related_name='chat', to='chat.Group_Name'),
        ),
    ]
