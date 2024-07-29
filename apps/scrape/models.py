from django.contrib.auth import get_user_model
from django.db import models


class Scrape(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    url = models.URLField()
    emails = models.TextField()  # Store emails as a comma-separated string
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scrape by {self.user.email} on {self.url}"
