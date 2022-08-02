from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if 'class' not in visible.field.widget.attrs:
                visible.field.widget.attrs['class'] = ''
            visible.field.widget.attrs['class'] += ' form-control'


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
