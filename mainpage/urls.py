from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView


router = DefaultRouter()
router.register('task',views.TaskViewSet)
router.register('profile',views.ProfilViewSet)

urlpatterns = [
    path("api/token/",TokenObtainPairView.as_view(),name='obtain-token'),
    path("api/token/refresh/",TokenRefreshView.as_view(),name='refresh-token'),
    path('api/register/', views.UserCreate.as_view(), name='user-register'),
    path("myprofile/",views.MyProfileView.as_view(),name='user-profile'),

]+router.urls