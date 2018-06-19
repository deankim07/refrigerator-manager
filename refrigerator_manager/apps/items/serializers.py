from rest_framework import serializers

from items.models import Vegetables


class VegetablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetables
        fields = '__all__'
