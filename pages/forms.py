from django import forms

from main.dictionary import exp
from main.forms import BootstrapForm


class ContactUsForm(BootstrapForm):
    title = forms.CharField(label=exp('contact_us.title'), min_length=1, max_length=50)
    email = forms.EmailField(label=exp('contact_us.email'), widget=forms.EmailInput(attrs={'class': 'force-ltr'}))
    text = forms.CharField(label=exp('contact_us.text'), min_length=10, max_length=250)
