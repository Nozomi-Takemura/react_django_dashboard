from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.apps


class CustomUserAdmin(UserAdmin):
    """
    A form to add and change user instances
    """
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
    # config. group and permisson 
    filter_horizontal = () 

    # removed username --> change the def. order
    ordering = ('email',)
    list_display = ('email','is_active','is_admin')
    list_filter = ('is_active','is_admin')

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ()}),
        ("Permissions",{
            "fields": (
                "is_active",
                "is_admin",
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
admin.site.register(get_user_model(), CustomUserAdmin)

# unregister teh Group model from adin
admin.site.unregister(Group)


