from django.db import models

# Create your models here.
class Pickup(models.Model):
    name = models.CharField(max_length=50, blank=True)
    mobilenumber = models.IntegerField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    latt = models.IntegerField()
    longitude = models.IntegerField()
    medicalemergency = models.BooleanField(default=False, blank=True)
    medicalreason = models.TextField(blank=True)
    no_people = models.IntegerField(blank=True)

    def __str__(self):
        return(self.name)
