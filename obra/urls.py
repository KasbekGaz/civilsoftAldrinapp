from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserRegistrationViewSet, UserLoginViewSet, UserLogoutViewSet


router = DefaultRouter()
router.register(r'registrouser', UserRegistrationViewSet,
                basename='registrouser')
router.register(r'loginuser', UserLoginViewSet, basename='loginuser')
router.register(r'logoutuser', UserLogoutViewSet, basename='logoutuser')


urlpatterns = [
    path('api/v1/', include(router.urls))
]
