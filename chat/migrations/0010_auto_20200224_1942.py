# Generated by Django 3.0.3 on 2020-02-24 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20200224_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group_name',
            old_name='usermanes',
            new_name='usernames',
        ),
    ]
