# Generated by Django 3.1.6 on 2021-02-19 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='anchor',
            new_name='author',
        ),
    ]
