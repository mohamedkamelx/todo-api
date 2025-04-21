from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tasks,Profile

class TaskSerializer(serializers.ModelSerializer):
    user=serializers.HyperlinkedRelatedField(read_only=True,view_name='profile-detail')
    class Meta:
        model=Tasks
        fields="__all__"


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','is_staff','last_login']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        

class ProfileSerializer(serializers.ModelSerializer):
    user=Userserializer(read_only=True)
    tasks=TaskSerializer(many=True, read_only=True) 
    class Meta:
        model=Profile
        fields=['user','tasks','score']

    