from django.dispatch import receiver
from django.db.models.signals import post_save
from Accounts.models import Account, UserProfile

@receiver(post_save, sender=Account)
def create_profile(sender, instance , created, **kwargs):
    user = instance
    if created:
        
        profile = UserProfile(user=user)
        
        profile.save()