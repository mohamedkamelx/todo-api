# signals.py (create new file if needed)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a profile automatically when a User is created"""
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()