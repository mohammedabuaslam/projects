from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2', 'phone', 'country',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class LoginForm(AuthenticationForm):
    user = get_user_model()
    username = forms.CharField(label='Email')
    if not user.is_active:
        raise forms.ValidationError(
            self.error_messages['inactive'],
            code='inactive',)

class UserPasswordResetForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)