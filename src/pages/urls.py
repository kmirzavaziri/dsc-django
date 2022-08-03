from django.urls import path

from .views import home_view, contact_us_view, contact_us_success_view

app_name = 'pages'
urlpatterns = [
    path('', home_view, name='home'),
    path('contact-us/', contact_us_view, name='contact_us'),
    path('contact-us-success/', contact_us_success_view, name='contact_us_success'),
]
