from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Tasks,Profile
from .serializers import TaskSerializer,ProfileSerializer,UserRegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_headers
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class TaskViewSet (viewsets.ModelViewSet):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    filter_backends=[SearchFilter,OrderingFilter]
    ordering=['title']
    search_fields=['title','description']

    pagination_class=PageNumberPagination
    pagination_class.page_size=5

    @method_decorator(cache_page(60*5,key_prefix='tasks'))
    @method_decorator(vary_on_headers('Authorization'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    def get_queryset(self):
        qs = super().get_queryset()
        p=Profile.objects.get(user=self.request.user)
        return qs.filter(user=p)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)
    
    
class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['user__username','tasks__title','tasks__description']
 
    queryset = Profile.objects.prefetch_related('tasks')
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
 
    pagination_class=PageNumberPagination
    pagination_class.page_size=5

    @method_decorator(cache_page(60*5, key_prefix='profiles'))
    @method_decorator(vary_on_headers('Authorization'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MyProfileView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    @method_decorator(cache_page(60*5,key_prefix='myprofile'))
    @method_decorator(vary_on_headers('Authorization'))
    def get(self,request):
        profile = Profile.objects.prefetch_related('tasks').get(user=request.user)
        serializer = ProfileSerializer(profile, context={'request': request})
        print(serializer.data)
        return Response(serializer.data)


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