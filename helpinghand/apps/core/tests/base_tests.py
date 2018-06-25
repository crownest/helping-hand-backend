# Third-Party
from rest_framework import status
from rest_framework.test import APITestCase

# Django
from django.urls import reverse

# Local Django
from users.models import User


class TokenAPITestCase(APITestCase):

    def setUp(self):
        # Create User
        self.email = 'helpinghand@unicrow.com'
        self.first_name = 'Crownest'
        self.last_name = 'Apps'
        self.password = '123456test'
        self.user = User.objects.create_user(
            email=self.email, password=self.password
        )
        self.user.first_name = self.first_name
        self.user.last_name = self.last_name
        self.user.save()
