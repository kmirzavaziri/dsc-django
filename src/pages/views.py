from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ContactUsForm
from utils import send_email


def home_view(request):
    return render(request, 'pages/home.html')


def contact_us_view(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd.get('title')
            email = cd.get('email')
            text = cd.get('text')
            body = f'text:\n{text}\n\nemail: {email}'
            send_email(subject=title, body=body, to_email='danial.erfanian@divar.ir', from_email='does@not.matter')
            return redirect(reverse('pages:contact_us_success'))
    else:
        form = ContactUsForm()

    return render(request, 'pages/contact_us.html', {'form': form})


def contact_us_success_view(request):
    return render(request, 'pages/contact_us_success.html')
