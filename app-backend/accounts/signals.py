from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomeUser,Profile


@receiver(post_save, sender=CustomeUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,pk=instance.pk)