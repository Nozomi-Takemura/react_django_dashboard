import uuid
# from django.apps import apps
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission, _user_has_module_perms, _user_has_perm    
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields.array import ArrayField
from django.core.validators import RegexValidator, EmailValidator
from django.utils.translation import gettext_lazy as _
from django.utils.itercompat import is_iterable

# test

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
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._custom_create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._custom_create_user(email, password, **extra_fields)

    # no change on def with_perm...

class ApplicationRoleManager(models.Manager):
    """
    The manager for the auth's Group model.
    """

    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class ApplicationRole(models.Model):
    """
    """
    # id: temporary skipped b.c. Group does not have it 

    # Name: string
    name = models.CharField(_("name"), max_length=150, unique=True)

    # Description: string(see in Jango how to regulate the string length. Here we need something not too long.)
    description = models.CharField(_("description"), max_length=150, unique=True)


    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("permissions"),
        blank=True,
    )

    objects = ApplicationRoleManager()

    class Meta:
        verbose_name = _("applicationrole")
        verbose_name_plural = _("applicationroles")

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)

# 99% just copy of PermissionsMixin...
class CustomPermissionsMixin(models.Model):
    """
    Add the fields and methods necessary to support the Group and Permission
    models using the ModelBackend.
    """
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )

    applicationroles = models.ManyToManyField(
        ApplicationRole,
        verbose_name=_("applicationroles"),
        blank=True,
        help_text=_(
            "The role this user is assigned to. A user will get all permissions "
            "granted to each of their roles."
        ),
        related_name="applicationuser_set",
        related_query_name="applicationuser",
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="applicationuser_set",
        related_query_name="applicationuser",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="applicationuser_set",
        related_query_name="applicationuser",
    )    

    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission. Query all
        available auth backends, but return immediately if any backend returns
        True. Thus, a user who has permission from a single auth backend is
        assumed to have permission in general. If an object is provided, check
        permissions for that object.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
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
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)

    # we don't want o create db table for this
    class Meta:
        abstract = True 

# Todo chained-drop down would be ideal 
class AddressModelMixin(models.Model):
    address1 = models.CharField('Address line 1', max_length=50)
    address2 = models.CharField('Address line 2', max_length=50, blank=True)
    city = models.CharField('City', max_length=20),
    state = models.CharField('State', max_length=20)
    zip_code = models.CharField('ZIP', max_length=12)
    company = models.CharField('Company', max_length=20) 

    class Meta:
        abstract = True

# eventually, this is just a copy and past from 'class AbstractUser'
# duplicated to allow us to customize later if necessary
# assumed the uniquness of email add <-- this can be changed by design...
# assumed that an account is linked to an email...
# e.g.
# An user subscribes a program with 20 accounts(he is an owner).
class ApplicationUser(AbstractBaseUser,CustomPermissionsMixin):
    #Id: string
     # not string
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    #FirstName: string
    first_name = models.CharField(_("first name"), max_length=150, blank=True)

    #AdditionalNames(optional): string[](In the databases we don’t have array, so we have to parse it.)
    additional_names = ArrayField(
        base_field = models.CharField(max_length=20,blank=True),
        verbose_name="additional names",
        size=10,
        null=True
    )

    #LastName: string
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
 
    #CreationDate: (see if there is special datatype in Jango) 
    creation_date = models.DateTimeField(_("creation date"), default=timezone.now)
    #AccountId: string
     # temporary remove b.c. this can be reachable via email
    accountid = models.ForeignKey(
        'ApplicationAccount',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
        # related_name = 'accounts',
        # related_name='owner_accountid'
    )

    #RoleId: string
    # inherit 'Group' from CustomPermissionsMixin class

    #Email Address
    email_validator = EmailValidator()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[email_validator],
        # error_messages={
        #   "unique": _("An user with that email already exists."),
        # },
    )

    #Phone Number
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        verbose_name="phone number",
        max_length=15,
        validators=[phone_regex],
    )


    # All other Jango specific needed fields for the credentials and etc.
    # username_validator = UnicodeUsernameValidator()
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()


    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # class Meta:
    #     verbose_name = _("user")
    #     verbose_name_plural = _("users")
    #     abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

# all the acounts including owner
class ApplicationAccount(AddressModelMixin):
    #id: string

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # Name: string
    name = models.CharField(_("name"), max_length=20, blank=True)
    
    # OwnerId: string
    ownerid = models.ForeignKey(
        'ApplicationUser',
        on_delete=models.CASCADE,
    )

    # Email: string(see if there is special datatype in Jagno)
    email_validator = EmailValidator()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=False,
        validators=[email_validator],
        # error_messages={
        #   "unique": _("An user with that email already exists."),
        # },
    )

    # Status: Enum(preferably - see Jagno)
    #    Submitted
    #    Approved
    #    Cancelled
    Submitted = 'S'
    Approved = 'A'
    Cancelled = 'C'
    STATUS = [
        (Submitted, 'Submitted'),
        (Approved, 'Approved'),
        (Cancelled, 'Cancelled'),    
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS,
    )

    # CreationDate: (see if there is special datatype in Jango)
    creation_date = models.DateTimeField(_("creation date"), default=timezone.now)

    # Address: string, City: string, State: string, ZIP: string, Company: string
    # <-- AddressModelMixin


class ApplicationArtifact(models.Model):
    # Id: string
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # AccountId: string
    accountid = models.ForeignKey(
        'ApplicationAccount',
        on_delete = models.CASCADE,
        # related_name='owner_accountid'
    )

    # CreatorId: string
    createrid = models.ForeignKey(
        'ApplicationUser',
        on_delete=models.CASCADE,
    )

    # ResourceKind: Enum(preferably - see Jango)
    #  RFDataContract
    #  MLModel
    #  MLInput
    #  RFModel
    RFDataContract = 'RFDataContract'
    MLModel = 'MLModel'
    MLInput = 'MLInput'
    RFModel = 'RFModel'
    RESOURCEKIND = [
        (RFDataContract, 'Reinforcement learning data contract'),
        (MLModel, 'Machine learning model'),
        (MLInput, 'Machine learning input data'),    
        (RFModel, 'Reinforcement learning model'),    
    ]
    resourcekind = models.CharField(
        max_length=20,
        choices=RESOURCEKIND,
    )    

    # IsAvtive: bool
    is_active = models.BooleanField(
        _("active"),
        default=True,
        # help_text=_(),
    )       
