from django.urls import path
from .views import hello, Register, Login, ChangePassword, TaskView, TaskDetailView, ArchiveTask, ArchievedTaskView, UnArchiveTask
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("hello/", hello, name="hello"),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('change-password/', ChangePassword.as_view(), name='change_password'),
    path('api-token-auth/', obtain_auth_token),
    path('todo/',TaskView.as_view(),name="todo"),
    path('todo/<int:pk>/',TaskDetailView.as_view()),
    path('archive-task/<int:pk>/',ArchiveTask.as_view(),name="archive-task"),
    path('archieved-task/',ArchievedTaskView.as_view(),name="archived-task"),
    path('unarchive-task/<int:pk>/', UnArchiveTask.as_view(), name="unarchive-task"),


]