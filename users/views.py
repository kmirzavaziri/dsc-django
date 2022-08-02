from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm
from .decorators import not_logged_in_required


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True


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
