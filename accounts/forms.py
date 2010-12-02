import settings

from django import forms
from django.contrib.auth.forms import UserCreationForm


class SecretField(forms.CharField):
    """A field which validates input against a set secret.
    """
    def validate(self, value):
        """Returns a boolean indicating whether the user has supplied
        the correct secret.
        """
        if value != settings.REGISTRATION_SECRET:
            raise forms.ValidationError('Incorrect Secret')

class RegistrationForm(UserCreationForm):
    secret = SecretField(max_length=50)
