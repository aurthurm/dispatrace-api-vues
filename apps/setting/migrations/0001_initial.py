# Generated by Django 2.2.6 on 2019-11-10 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo_serial_commenting', models.BooleanField(default=True, verbose_name='Enforce Memorandum Serial Commenting')),
                ('action_reauth', models.BooleanField(default=True, verbose_name='Enforce action re-authentication')),
            ],
        ),
    ]
