from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse

User = get_user_model()


class UserAPITestCase(APITestCase):

    def setUp(self):
        self.admin_user = User.objects.create_superuser(email='admin1@gmail.com', password='admin123')
        self.regular_user = User.objects.create_user(email='user1@gmail.com', password='user123')
        self.register_url = reverse('user-register')
        self.login_url = reverse('user-login')
        self.profile_url = lambda pk: reverse('user-profile', kwargs={'pk': pk})
        self.list_users_url = reverse('user-list-users')
        self.delete_user_url = lambda pk: reverse('user-delete-user', kwargs={'pk': pk})

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_register(self):
        data = {
            'email': 'newuser1@gmail.com',
            'password': 'newuser123',
            'first_name': 'New',
            'last_name': 'User'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        data = {
            'email': 'user1@gmail.com',
            'password': 'user123'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_profile(self):
        token = self.get_token(self.regular_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(self.profile_url(self.regular_user.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        update_data = {'first_name': 'LoL'}
        response = self.client.put(self.profile_url(self.regular_user.pk), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'LoL')

    def test_list_users(self):
        token = self.get_token(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(self.list_users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_delete_user(self):
        token = self.get_token(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.delete(self.delete_user_url(self.regular_user.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(self.profile_url(self.regular_user.pk))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
