import collections

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from items.models import Vegetables
from users.tests.factories import UserFactory
from items.tests.factories import VegetablesFakeFactory, ForksFakeFactory
from place.tests.factories import PlaceFakeFactory


class VegetablesListCreateAPIViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.vegtable = VegetablesFakeFactory.create(user=cls.user)
        cls.place = PlaceFakeFactory.create(user=cls.user)

    def setUp(self):
        self.client.login(username=self.user.username, password='password')
        self.url = reverse('query_for_vegetables_list')

    def test_can_get_vegetable_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['category'], self.vegtable.category)

    def test_can_create_vegetable(self):
        data = {
            'user': self.user.id,
            'category': 'PAPRIKA',
            'quantity': 12.0,
            'place': self.place.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['quantity'], str(data['quantity']))


class VegetableItemRetrieveUpdateDeleteViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.vegtable = VegetablesFakeFactory.create(user=cls.user)

    def setUp(self):
        self.client.login(username=self.user.username, password='password')
        self.url = reverse('retrieve_update_delete_vegetable_item', kwargs={'vegetable_id': self.vegtable.id})

    def test_can_retrieve_vegetable_item(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], self.vegtable.category)

    def test_can_update_vegetable_item(self):
        patch_data = {
            'quantity': 10.0
        }
        response = self.client.patch(self.url, patch_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], str(patch_data['quantity']))


class ForksListCreateAPIViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.fork = ForksFakeFactory.create(user=cls.user)
        cls.place = PlaceFakeFactory.create(user=cls.user)

    def setUp(self):
        self.client.login(username=self.user.username, password='password')
        self.url = reverse('query_for_forks_list')

    def test_can_get_fork_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['category'], self.fork.category)

    def test_can_create_fork(self):
        data = {
            'user': self.user.id,
            'category': 'LOIN',
            'quantity': 7,
            'place': self.place.id,
            'gram_per_package': 100
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['quantity'], data['quantity'])


class ForkItemRetrieveUpdateDeleteViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.fork = ForksFakeFactory.create(user=cls.user)

    def setUp(self):
        self.client.login(username=self.user.username, password='password')
        self.url = reverse('retrieve_update_delete_fork_item', kwargs={'fork_id': self.fork.id})

    def test_can_retrieve_fork_item(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], self.fork.category)

    def test_can_update_fork_item(self):
        patch_data = {
            'gram_per_package': 90.0
        }
        response = self.client.patch(self.url, patch_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['gram_per_package'], str(patch_data['gram_per_package']))



