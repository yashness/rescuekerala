from django.urls import path
from . import views

urlpatterns = [
    path('requesthelp/<int:pk>/',views.EmergencyPickup.as_view(),name='EmergencyPickup'),
    path('requesthelp/',views.EmergencyPickupList.as_view(),name='EmergencyPickup'),


]
