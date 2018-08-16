from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class EmergencyPickup(generics.RetrieveUpdateAPIView):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer
