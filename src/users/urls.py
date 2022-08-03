from django.urls import path

from .views import CustomLoginView, logout_view, register_view, profile_view, setting_view, TeacherListView, \
    TeacherListApiView, delete_me

app_name = 'users'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('users/<str:username>/', profile_view, name='profile'),
    path('setting/', setting_view, name='setting'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list'),
    path('search_teacher_api/', TeacherListApiView.as_view(), name='teacher_list'),
    path('delete/', delete_me, name='delete'),
]
