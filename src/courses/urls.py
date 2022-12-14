from django.urls import path

from .views import CourseListView, CreateCourseView, UpdateCourseView, delete_course_view

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('0/', CreateCourseView.as_view(), name='new'),
    path('<int:pk>/', UpdateCourseView.as_view(), name='detail'),
    path('<int:pk>/delete', delete_course_view, name='delete'),
]
