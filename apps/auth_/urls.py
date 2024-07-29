from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'auth', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/profile/<int:pk>/', UserViewSet.as_view({'get': 'profile', 'put': 'profile'}), name='user-profile'),
    path('auth/register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('auth/login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('auth/list_users/', UserViewSet.as_view({'get': 'list_users'}), name='user-list-users'),
    path('auth/delete_user/<int:pk>/', UserViewSet.as_view({'delete': 'delete_user'}), name='user-delete-user'),
]