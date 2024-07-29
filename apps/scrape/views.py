import re

import requests
from bs4 import BeautifulSoup

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.scrape.models import Scrape
from apps.scrape.serializers import ScrapeSerializer


class ScrapeViewSet(viewsets.ModelViewSet):
    serializer_class = ScrapeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Scrape.objects.all()
        return Scrape.objects.filter(user=user)

    def perform_create(self, serializer):
        url = serializer.validated_data['url']
        emails = self.scrape_emails(url)
        serializer.save(user=self.request.user, emails=emails)

    def scrape_emails(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text()))
        return ', '.join(emails)

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def list_scrapes(self, request):
        scrapes = self.get_queryset()
        serializer = ScrapeSerializer(scrapes, many=True)
        return Response(serializer.data)
