from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import ApplicationUser, ApplicationAccount
from django.contrib.auth import get_user_model # ~=ApplicationUser

custom_user = get_user_model()
# whenever ApplicationUser gets created, Account gets created as well
@receiver(signal=post_save, sender=custom_user)
def create_account(sender, instance, **kwargs):
    if instance.accountid == None:
        applicationaccount = ApplicationAccount.objects.create(ownerid=instance)
        instance.accountid = applicationaccount

# @receiver(signal=pre_save, sender=ApplicationAccount)
# def handle_ownerid(sender, instance, **kwargs):
#     owner = custom_user.objects.filter(pk=)  
#     applicationaccount = ApplicationAccount.objects.create()
#     instance.accountid = applicationaccount.id