from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('users.urls')),
    path('panel/', include('panel.urls')),
    path('panel/courses/', include('courses.urls')),
]