# Generated by Django 2.2.6 on 2019-10-23 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='name',
            new_name='title',
        ),
    ]
