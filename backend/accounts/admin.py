from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import ApplicationUser
from .forms import ApplicationUserChangeForm, ApplicationUserCreationForm
# Register your models here.apps


class ApplicationUserAdmin(UserAdmin):
    """
    A form to add and change user instances
    """
    form = ApplicationUserChangeForm
    add_form = ApplicationUserCreationForm
    
    # config. group and permisson 
    filter_horizontal = () 

    # removed username --> change the def. order
    ordering = ('email',)
    list_display = ('email','is_active','is_staff','first_name','last_name','additional_names','phone_number','creation_date','accountid')
    list_filter = ('is_active','is_staff')

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ()}),
        ("Permissions",{
            "fields": (
                "is_active",
                "is_staff",
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'class': ('wide',),
            'fields': ("email", 'password1', 'password2'),
        }),
    )

    search_field = ('email',)

# register the new UserAdmin
admin.site.register(get_user_model(), ApplicationUserAdmin)



