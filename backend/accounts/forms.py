from django import forms
from django.contrib.auth import get_user_model
# Register your models here.apps

class CustomUserCreationForm(forms.ModelForm):
    """
    A form for creating new users.
    """
    class Meta:
        model = get_user_model()
        fields = ('email',)
    pass

class CustomUserChangeForm(forms.ModelForm):
    """
    A form for updating users.
    """
    class Meta:
        model = get_user_model()
        fields = ('email','password','is_active','is_admin')
