from django.urls import path

from .views import CustomLoginView, logout_view, register_view, profile_view, setting_view

app_name = 'users'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('setting/', setting_view, name='setting'),
]
