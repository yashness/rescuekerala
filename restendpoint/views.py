from django.shortcuts import render
from rest_framework import generics
from .models import Pickup
from .serializers import PickupSerializer

# Create your views here.
class EmergencyPickup(generics.RetrieveUpdateAPIView):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer

class EmergencyPickupList(generics.ListCreateAPIView):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer
