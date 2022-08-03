from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_http_methods

from main.views import ApiListView
from .forms import RegistrationForm, LoginForm, SettingForm
from .decorators import not_logged_in_required
from .models import User


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True


def logout_view(request):
    logout(request)
    return redirect(reverse('pages:home'))


@not_logged_in_required
@require_http_methods(["GET", "POST"])
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


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'user': user})


@login_required
@require_http_methods(["GET", "POST"])
def setting_view(request):
    if request.method == 'POST':
        form = SettingForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = SettingForm(instance=request.user)
    return render(request, 'users/setting.html', {'form': form})


class TeacherListView(generic.ListView):
    model = User
    template_name = 'users/teacher_list_view.html'

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.filter(type=User.Type.TEACHER)

        text = self.request.GET.get('q')
        if text:
            qs = qs.filter(
                Q(first_name__contains=text) |
                Q(last_name__contains=text) |
                Q(username__contains=text)
            )
        else:
            qs = qs.none()

        return qs


class TeacherListApiView(ApiListView):
    model = User
    template_name = 'users/teacher_list_view.html'

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.filter(type=User.Type.TEACHER)

        text = self.request.GET.get('query')
        if text:
            qs = qs.filter(
                Q(first_name__contains=text) |
                Q(last_name__contains=text) |
                Q(username__contains=text)
            )
        else:
            qs = qs.none()

        return qs

    def response_data(self):
        data = []
        for user in self.object_list:
            data.append({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'url': reverse('users:profile', args=(user.username, )),
            })
        return data
