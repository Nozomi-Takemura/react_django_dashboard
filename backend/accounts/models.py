import uuid
# from django.apps import apps
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields.array import ArrayField
from django.core.validators import RegexValidator

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
        assumefrom django.core.validators import RegexValidator

class PhoneModel(models.Model):
    ...
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
d to have permission in general. If an object is provided, check
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
    
    # property -- getter func
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # design - all admins are staff
        return self.is_admin

# class ApplicationAccount():
#     pass
# class ApplicationArtifact():
#     pass
# class ApplicationRole():
#     pass
# q. can we use "User"? --> Django default
class ApplicationUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # not string
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    # we use json here
    # To do
    # add en/de-coder here to parse the field
    additionalnames = ArrayField(base_field=models.CharField(max_length=20),verbose_name="additional names",size=10)
    creationdate = models.DateTimeField(
        verbose_name="create date",
        default = timezone.now(),
        max_length=20
    )
    accountid = models.CharField(max_length=50)
    roleid = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(verbose_name="phone number",validators=(phone_regex,), max_length=15)




"""
    ApplicationAccount:

        Id: string

        Name: string

        OwnerId: string

        Email: string(see if there is special datatype in Jagno)

        Status: Enum(preferably - see Jagno)

            Submitted

            Approved

            Cancelled

        CreationDate: (see if there is special datatype in Jango)

        Address: string

        City: string

        State: string

        ZIP: string

        Company: string

    ApplicationArtifact

        Id: string

        AccountId: string

        CreatorId: string

        ResourceKind: Enum(preferably - see Jango)

            RFDataContract

            MLModel

            MLInput

            RFModel

            …

        IsAvtive: bool

    ApplicationRole

        Id: string

        Name: string

        Description: string(see in Jango how to regulate the string length. Here we need something not too long.)

        All other Jango specific needed fields.

    ApplicationUser

        Id: string

        FirstName: string

        AdditionalNames(optional): string[](In the databases we don’t have array, so we have to parse it.)

        LastName: string

        CreationDate: (see if there is special datatype in Jango) 

        AccountId: string

        RoleId: string

        Email Address

        Phone Number

        All other Jango specific needed fields for the credentials and etc.
"""