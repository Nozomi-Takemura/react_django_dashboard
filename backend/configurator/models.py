import uuid
from django.db import models
from django.contrib.auth import get_user_model
# from accounts.models import ApplicationUser as User

# Create your models here.
class Setting(models.Model):
    
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable=False
    )

    settingname = models.CharField(
        max_length = 40,
        unique=True,
    )
    
    settingvalue = models.CharField(
        max_length = 40,
        null=True,
    )

    owner = models.ForeignKey(
        get_user_model(),
        related_name = 'settings',
        on_delete = models.CASCADE,
    )

    group = models.ForeignKey(
        'configurator.settinggroup',
        related_name = 'settings',
        on_delete = models.CASCADE,
        null = True,
    )

    def __str__(self):
        return '%s: %s' % (self.settingname, self.settingvalue)

class SettingGroup(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )

    groupname = models.CharField(
        max_length = 20,
    ) 

    owner = models.ForeignKey(
        get_user_model(),
        related_name = 'settinggroups',
        on_delete = models.CASCADE,
        null = True
    )
