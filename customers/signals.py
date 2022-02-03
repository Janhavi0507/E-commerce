from .models import Account, Customer
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Customer)
def create_account(sender, instance, created, **kwargs):
  if created:
    Account.objects.create(User=instance)