# Generated by Django 3.0.3 on 2020-02-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20200224_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='description',
            field=models.TextField(default='Type Chat Room Description Here...'),
            preserve_default=False,
        ),
    ]
