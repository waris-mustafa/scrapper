from rest_framework import serializers

from .models import EmailSender


class EmailSenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSender
        fields = '__all__'
        read_only_fields = ('user', 'scrape', 'created_at', 'updated_at')
