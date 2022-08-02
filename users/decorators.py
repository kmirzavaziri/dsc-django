from django.shortcuts import redirect
from django.urls import reverse


def not_logged_in_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('pages:home'))
        return func(request, *args, **kwargs)
    return wrapper
