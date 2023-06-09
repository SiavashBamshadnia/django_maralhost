from rest_framework import serializers

from ecommerce import models


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = '__all__'
