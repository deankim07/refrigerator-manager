import factory

from core.constant import PlaceConstant


class PlaceFakeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'place.Place'

    name = factory.Iterator(iterator=(type for type, _ in PlaceConstant.TYPE))