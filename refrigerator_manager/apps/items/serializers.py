from rest_framework import serializers

from items.models import Vegetables, Forks


class VegetablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetables
        fields = '__all__'


class ForksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forks
        fields = '__all__'