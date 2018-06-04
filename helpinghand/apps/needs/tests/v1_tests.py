# Standard Library
import datetime

# Third-Party
from rest_framework import status

# Django
from django.urls import reverse

# Local Django
from .base_tests import NeedAPITestCase


class NeedAPITestCaseV1(NeedAPITestCase):

    def test_list_need(self):
        url = reverse('v1:needs-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
