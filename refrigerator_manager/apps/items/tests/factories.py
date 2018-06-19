import factory

from datetime import timedelta
from django.utils import timezone

from place.tests.factories import PlaceFakeFactory
from core.constant import VegetableConstant
from users.tests.factories import UserFactory


class VegetablesFakeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'items.Vegetables'

    place = factory.SubFactory(PlaceFakeFactory)
    category = VegetableConstant.PAPRIKA
    save_begin = factory.Faker('date')
    storage_period = 7
    quantity = 3
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def left_storage_period(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            days = timedelta(days=float(str(self.storage_period)))
            dead_line = self.save_begin + days
            left_days = dead_line - timezone.now().date()
            return left_days
