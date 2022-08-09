from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)  + six.text_type(user.is_active)
        )

class UserPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    User = get_user_model()
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)
        )

account_activation_token = AccountActivationTokenGenerator()
user_password_reset_token = UserPasswordResetTokenGenerator()