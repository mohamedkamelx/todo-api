from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Tasks,Profile
from .serializers import TaskSerializer,ProfileSerializer,UserRegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
# Create your views here.

class TaskViewSet (viewsets.ModelViewSet):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get_queryset(self):
        qs = super().get_queryset()
        p=Profile.objects.get(user=self.request.user)
        return qs.filter(user=p)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)
    
    
class ProfilViewSet (viewsets.ReadOnlyModelViewSet):
    queryset=Profile.objects.prefetch_related('tasks')
    serializer_class=ProfileSerializer
    permission_classes=[IsAdminUser]
    authentication_classes=[JWTAuthentication]

"""    
class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self,request):
        if request.user.is_staff:
            profiles = Profile.objects.select_related('user').prefetch_related('user__tasks')
            serializer = ProfileSerializer(profiles,many=True)
            return Response(serializer.data)
        return Response('you are not allowed 🖕',404)

    def get(self,request,pk):
        try:
            user=User.objects.get(pk=pk)
        except:
            return Response('doesnt exist',404)
        if request.user==user:
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        return Response('you are not allowed 🖕',404)"""


class UserCreate(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            print(1)
            user = serializer.save()
            print(2)
            refresh = RefreshToken.for_user(user)
            print(12)
            return Response(
                {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
                status=201
            )
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        return Response({'message': 'Enter username and password to register'})