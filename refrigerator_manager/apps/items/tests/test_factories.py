from django.contrib.auth import get_user_model
from django.test import TestCase

from users.tests.factories import UserFactory

from items.models import Paprika
from items.tests.factories import PaprikaFakeFactory

User = get_user_model()


class PaprikaFakeFactoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.paprika = PaprikaFakeFactory.create(user=cls.user)

    def test_user_created(self):
        self.assertIn('user-', self.user.username)

    def test_paprika_can_create(self):
        self.assertEqual(Paprika.objects.count(), 1)
        print(Paprika.objects.first().left_storage_period)
        self.assertEqual(Paprika.objects.first().user_id, self.user.id)