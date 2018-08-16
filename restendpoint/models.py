from django.db import models

# Create your models here.
class Pickup(models.Model):
    name = models.CharField(max_length=50)
    mobilenumber = models.IntegerField()
    location = models.CharField(max_length=100)
    latt = models.IntegerField()
    long = models.IntegerField()
    medicalemergency = models.TextField()
    no_people = models.IntegerField()

    def __str__(self):
        return(self.name)
