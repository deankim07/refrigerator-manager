import collections

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from items.models import Vegetables
from users.tests.factories import UserFactory
from items.tests.factories import VegetablesFakeFactory


class VegetablesListCreateAPIViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.vegtable = VegetablesFakeFactory.create(user=cls.user)

    def setUp(self):
        self.client.login(username=self.user.username, password='password')
        self.url = reverse('query_for_vegetables')

    def test_can_get_vegetables(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
