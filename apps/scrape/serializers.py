from rest_framework import serializers

from .models import Scrape


class ScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrape
        fields = ['id', 'user', 'url', 'emails', 'created_at']
        read_only_fields = ['id', 'user', 'emails', 'created_at']
