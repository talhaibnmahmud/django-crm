from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save

from .models import Customer


def customer_profile(sender, instance, created: bool, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(user=instance, name=instance.username,)


post_save.connect(customer_profile, sender=User)
