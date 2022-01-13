from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Datos
from django.dispatch import receiver

@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        Datos.objects.create(usuario=instance)