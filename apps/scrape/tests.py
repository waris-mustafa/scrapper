from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from apps.scrape.models import Scrape

CustomUser = get_user_model()

class ScrapeTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='user@example.com', password='password')
        self.admin = CustomUser.objects.create_superuser(email='admin@example.com', password='password')
        self.client = APIClient()

    def test_user_can_view_own_scrapes(self):
        self.client.force_authenticate(user=self.user)
        scrape = Scrape.objects.create(user=self.user, url='https://www.zoho.com/mail/how-to/choose-a-professional-email-address.html', emails='test@example.com')
        response = self.client.get(reverse('scrape-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['emails'], 'test@example.com')

    def test_user_cannot_view_others_scrapes(self):
        other_user = CustomUser.objects.create_user(email='other@example.com', password='password')
        Scrape.objects.create(user=other_user, url='http://example.com', emails='test@example.com')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('scrape-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_admin_can_view_all_scrapes(self):
        self.client.force_authenticate(user=self.admin)
        Scrape.objects.create(user=self.user, url='https://www.zoho.com/mail/how-to/choose-a-professional-email-address.html', emails='test@example.com')
        response = self.client.get(reverse('scrape-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_user_can_create_scrape(self):
        self.client.force_authenticate(user=self.user)
        data = {'url': 'https://www.zoho.com/mail/how-to/choose-a-professional-email-address.html'}
        response = self.client.post(reverse('scrape-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Scrape.objects.count(), 1)
        self.assertEqual(Scrape.objects.get().user, self.user)

    def test_admin_can_view_individual_scrape(self):
        self.client.force_authenticate(user=self.admin)
        scrape = Scrape.objects.create(user=self.user, url='https://www.zoho.com/mail/how-to/choose-a-professional-email-address.html', emails='test@example.com')
        response = self.client.get(reverse('scrape-detail', args=[scrape.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['emails'], 'test@example.com')

    def test_user_cannot_view_individual_scrape_of_others(self):
        other_user = CustomUser.objects.create_user(email='other@example.com', password='password')
        scrape = Scrape.objects.create(user=other_user, url='https://www.zoho.com/mail/how-to/choose-a-professional-email-address.html', emails='test@example.com')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('scrape-detail', args=[scrape.id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)