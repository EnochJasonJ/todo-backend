from django.urls import path, include
from .views import hello, Register, Login, ChangePassword, TaskView, TaskDetailView, ArchiveTask, ArchievedTaskView, UnArchiveTask
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("hello/", hello),
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('change-password/', ChangePassword.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('todo/', TaskView.as_view()),
    path('todo/<int:pk>/', TaskDetailView.as_view()),
    path('archive-task/<int:pk>/', ArchiveTask.as_view()),
    path('archieved-task/', ArchievedTaskView.as_view()),
    path('unarchive-task/<int:pk>/', UnArchiveTask.as_view()),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
