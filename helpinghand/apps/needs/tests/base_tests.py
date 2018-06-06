# Standard Library
import datetime

# Third-Party
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Local Django
from users.models import User
from needs.models import Need
from categories.models import Category


class NeedAPITestCase(APITestCase):

    def setUp(self):
        # Create User and Token
        self.user = User.objects.create_user('helpinghand@unicrow.com', '123456test')
        self.user.first_name = 'Helpinghand'
        self.user.last_name = 'Apps'
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        # Token Authentication
        self.api_authentication()

        # Test date
        self.date = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)

        # Create Category
        self.category = Category(name='Clothing')
        self.category.save()

        # Create Need
        self.title = 'Need shoes'
        self.is_fixed = True
        self.description = 'In need of shoes for my son.'
        self.address = 'Prins Bernhardstraat 13'
        self.need = Need(title=self.title, description=self.description, address=self.address,
                         end_date=self.date, is_fixed=self.is_fixed, creator=self.user,
                         )
        self.need.save()
        self.need.categories.add(self.category)
        self.need.supporters.add(self.user)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
