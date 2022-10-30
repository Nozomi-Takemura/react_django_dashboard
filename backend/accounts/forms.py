from django import forms
from django.contrib.auth import get_user_model
# Register your models here.apps

class ApplicationUserCreationForm(forms.ModelForm):
    """
    A form for creating new users.
    """
    class Meta:
        model = get_user_model()
        fields = ('email',)

class ApplicationUserChangeForm(forms.ModelForm):
    """
    A form for updating users.
    """
    class Meta:
        model = get_user_model()
        fields = ('email','password','email','is_active','is_staff','first_name','last_name','additional_names','phone_number','creation_date')
