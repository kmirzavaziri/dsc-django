from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from main.dictionary import exp
from main.forms import BootstrapForm

from .models import User


class RegistrationForm(BootstrapForm, UserCreationForm):
    error_messages = {
        'password_mismatch': exp('register.error_messages.password_mismatch'),
    }

    class Meta:
        model = User
        fields = ['type', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
        }
        error_messages = {
            'username': {
                'unique': exp('register.error_messages.unique_username'),
            }
        }


class LoginForm(BootstrapForm, AuthenticationForm):
    pass


class SettingForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'bio', 'image']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name if first_name else self.instance.first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name if last_name else self.instance.last_name
