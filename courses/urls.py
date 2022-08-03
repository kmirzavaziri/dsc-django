from django.urls import path

from .views import course_list_view, CreateCourseView, UpdateCourseView

app_name = 'courses'
urlpatterns = [
    path('', course_list_view, name='list'),
    path('0/', CreateCourseView.as_view(), name='new'),
    path('<int:pk>/', UpdateCourseView.as_view(), name='detail'),
]
