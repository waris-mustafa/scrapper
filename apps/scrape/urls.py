from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ScrapeViewSet

router = DefaultRouter()
router.register(r'scrapes', ScrapeViewSet, basename='scrape')

urlpatterns = [path('', include(router.urls)),]
