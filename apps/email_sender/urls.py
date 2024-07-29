from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SendEmailsView

router = DefaultRouter()

urlpatterns = [path('', include(router.urls)), path('send-emails/', SendEmailsView.as_view(), name='send-emails'), ]
