from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from apps.scrape.models import Scrape


@shared_task
def send_email_task(user_id):
    emails = Scrape.objects.filter(user_id=user_id)
    for email in emails:
        send_mail(subject=email.subject, message=email.message, from_email='', recipient_list=[email.email])
        email.sent_at = timezone.now()
        email.save()
