from django.db.models.signals import post_save, pre_save, m2m_changed
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from apps.accounts.models import AccountProfile

def auto_create_profile(instance, sender, **kwargs):
    """
    Once a User is created, let the profile be ato created too
    """
    if kwargs['created'] == True:
        user = instance
        AccountProfile.objects.get_or_create(user=user)

post_save.connect(auto_create_profile, sender=User)
