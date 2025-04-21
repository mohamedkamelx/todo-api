from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile,Tasks
from django.core.cache import cache
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a profile automatically when a User is created"""
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


@receiver([post_delete,post_save],sender=Profile)
def delete_cache_profiles(sender,instance,**kwargs):
    cache.delete_pattern("*myprofile*")
    cache.delete_pattern("*profiles*")



@receiver([post_delete,post_save],sender=Tasks)
def delete_cache_tasks(sender,instance,**kwargs):
    cache.delete_pattern("*myprofile*")
    cache.delete_pattern("*profiles*")
    cache.delete_pattern("*tasks*")
