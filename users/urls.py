from django.urls import path

from .views import CustomLoginView, register_view

app_name = 'users'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
]
