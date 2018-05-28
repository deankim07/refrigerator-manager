from django.contrib.auth import get_user_model
from django.test import TestCase

from users.tests.factories import UserFactory

from place.models import Place
from place.tests.factories import PlaceFakeFactory

User = get_user_model()


class PlaceFakeFactoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.paprika = PlaceFakeFactory.create(user=cls.user)

    def test_user_created(self):
        self.assertIn('user-', self.user.username)

    def test_paprika_can_create(self):
        self.assertEqual(Place.objects.count(), 1)
        self.assertEqual(Place.objects.first().user_id, self.user.id)