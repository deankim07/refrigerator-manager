from django.contrib.auth import get_user_model
from django.test import TestCase

from users.tests.factories import UserFactory

from items.models import Vegetables, Forks
from items.tests.factories import VegetablesFakeFactory, ForksFakeFactory

User = get_user_model()


class PaprikaFakeFactoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.paprika = VegetablesFakeFactory.create(user=cls.user)

    def test_user_created(self):
        self.assertIn('user-', self.user.username)

    def test_paprika_can_create(self):
        self.assertEqual(Vegetables.objects.count(), 1)
        self.assertEqual(Vegetables.objects.first().user_id, self.user.id)


class ForkFakeFactoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.fork = ForksFakeFactory.create(user=cls.user)

    def test_user_created(self):
        self.assertIn('user-', self.user.username)

    def test_paprika_can_create(self):
        self.assertEqual(Forks.objects.count(), 1)
        self.assertEqual(Forks.objects.first().user_id, self.user.id)