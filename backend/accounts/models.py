# from django.apps import apps
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.hashers import make_password
from django.db import models
# Create your models here.

class CustomUserManager(BaseUserManager):
    # not all [username,email,is_staff,is_active, 
    # is_superuser,last_login,date_joined]
    # are defined in CustomUser.
    # UserManger need to be defined.
    # def create_user(self, email, password=None):
    #     """
    #     Creates and saves a User with the given email and password.
    #     """  

    use_in_migrations = True

    def _custom_create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # ?
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        # GlobalUserModel = apps.get_model(
        #     self.model._meta.app_label, self.model._meta.object_name
        # )
        # username = GlobalUserModel.normalize_username(username)
        # ?
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", False)
        return self._custom_create_user(email, password, **extra_fields)

    def create_superuser(self,email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Admin must have is_admin=True.")

        return self._custom_create_user(email, password, **extra_fields)

    # no change on def with_perm...

class CustomPermissionsMixin(models.Model):
    """
    Add the fields and methods necessary to support the Group and Permission
    models using the ModelBackend.
    """
    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission. Query all
        available auth backends, but return immediately if any backend returns
        True. Thus, a user who has permission from a single auth backend is
        assumed to have permission in general. If an object is provided, check
        permissions for that object.
        """
        # Active admins have all permissions.
        if self.is_active and self.is_admin:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        """
        Return True if the user has each of the specified permissions. If
        object is passed, check if the user has all required perms for it.
        """
        if not is_iterable(perm_list) or isinstance(perm_list, str):
            raise ValueError("perm_list must be an iterable of permissions.")
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        """
        Return True if the user has any permissions in the given app label.
        Use similar logic as has_perm(), above.
        """
        # Active admins have all permissions.
        if self.is_active and self.is_admin:
            return True

        return _user_has_module_perms(self, app_label)

class CustomUser(AbstractBaseUser,CustomPermissionsMixin):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)   
    
    # set the unique identifier 
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # design - all admins are staff
        return self.is_admin
