from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from main.forms import BootstrapForm


class RegistrationForm(BootstrapForm, UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }


class LoginForm(BootstrapForm, AuthenticationForm):
    pass
