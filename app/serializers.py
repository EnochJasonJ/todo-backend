from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TaskModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Use the Django auth User model
        fields = ('username', 'password','email')
        # read_only_fields = ('password',)  # Make id read-only
        extra_kwargs = {
            'password': {'write_only': True}  # Make password write-only
        }
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id','title','priority','created_at','is_completed','is_archived']
    
    def create(self, validated_data):
        user = self.context['request'].user
        return TaskModel.objects.create(user=user,**validated_data)