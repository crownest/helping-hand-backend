# Standard Library
import datetime

# Third-Party
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Local Django
from users.models import User
from needs.models import Need


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

        # Create Need
        self.need = Need.objects.create(
            title='Need shoes', description='In need of shoes for my son.', address='Prins Bernhardstraat 13',
            end_date=datetime.datetime.strptime(self.date_str, '%Y-%m-%dT%H:%M:%S'),
            is_fixed=False, creator=self.user, categories='Clothing', supporters=''
        )

        # Create Dummy Data
        self.date = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        self.date_str = self.date.strftime('%Y-%m-%dT%H:%M:%S')
        self.dummy_data = {
            'need': self.need.id,
            'date': self.date_str
        }

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

