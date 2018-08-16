from rest_framework import serializers
from . models import Pickup

class PickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pickup
        exclude = ('latt','long')
