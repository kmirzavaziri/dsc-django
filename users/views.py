from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import RegistrationForm
from .decorators import not_logged_in_required


@not_logged_in_required
def login_view(request):
    return render(request, '')


@not_logged_in_required
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('pages:home')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})