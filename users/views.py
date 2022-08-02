from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegistrationForm, LoginForm, SettingForm
from .decorators import not_logged_in_required


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True


def logout_view(request):
    logout(request)
    return redirect(reverse('pages:home'))


@not_logged_in_required
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pages:home')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def profile_view(request):
    return render(request, 'users/profile.html')


@login_required
def setting_view(request):
    if request.method == 'POST':
        form = SettingForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = SettingForm(instance=request.user)
    return render(request, 'users/setting.html', {'form': form})
