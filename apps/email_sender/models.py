from django.db import models

from apps.auth_.models import CustomUser
from apps.scrape.models import Scrape


class EmailSender(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    scrape = models.ForeignKey(Scrape, on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
