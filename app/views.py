from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import UserSerializer, TaskSerializer
from .models import TaskModel
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.

from django.http import HttpResponse

def hello(request):
  return HttpResponse('Hello World!')


class Register(ListCreateAPIView):
    """
    API endpoint that allows users to be created.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()  # Save the new user instance

class Login(APIView):
   def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message":"Login Successful","token":token.key},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)
        
class ChangePassword(APIView):
    def post(self, request):
        username = request.data.get('username')
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not all([username, old_password, new_password]):
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=old_password)

        if user is  None:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
    

class TaskView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskModel.objects.filter(user = self.request.user, is_archived = False)

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskModel.objects.filter(user = self.request.user)
    
class ArchiveTask(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self,request,pk):
        try:
            task = TaskModel.objects.get(pk=pk, user=request.user)
            task.is_archived = True
            task.save()
            return Response({"message": "Task Archived!"}, status=status.HTTP_200_OK)
        except TaskModel.DoesNotExist:
            return Response({"message": "Task Not Found!"}, status=status.HTTP_404_NOT_FOUND)

class UnArchiveTask(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self,request,pk):
        try:
            task = TaskModel.objects.get(pk=pk, user=request.user)
            task.is_archived = False
            task.save()
            return Response({"message": "Task Unarchived!"}, status=status.HTTP_200_OK)
        except TaskModel.DoesNotExist:
            return Response({"message": "Task Not Found!"}, status=status.HTTP_404_NOT_FOUND)


class ArchievedTaskView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskModel.objects.filter(user = self.request.user, is_archived = True)