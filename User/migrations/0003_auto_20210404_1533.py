# Generated by Django 3.1.6 on 2021-04-04 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_reply_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='reply',
            new_name='replys',
        ),
    ]