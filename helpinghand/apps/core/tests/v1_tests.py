# Third-Party
from rest_framework import status

# Django
from django.urls import reverse

# Local Django
from core.tests import TokenAPITestCase


class TokenAPITestCaseV1(TokenAPITestCase):

    def test_login_auth(self):
        dummy_data = {
            'email': self.email,
            'password': self.password
        }
        url = reverse('auth-v1-login')

        response = self.client.post(url, dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
