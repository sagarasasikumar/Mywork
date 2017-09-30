from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


def get_choices(options):
    return zip([slugify(x) for x in options], options)

blood_group_choices = get_choices(['A+ve', 'A-ve', 'B+ve', 'B-ve', 'O+ve', 'O-ve', 'AB+ve', 'AB-ve'])
organ_choices = get_choices(['Heart', 'A-ve', 'B+ve', 'B-ve', 'O+ve', 'O-ve', 'AB+ve', 'AB-ve'])
# create your models here.

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.latitude)+","+str(self.longitude)
        # return str(self.address)

class Hospital(User):
    name = models.CharField(max_length = 100)
    location = models.ForeignKey(Location, null = True, blank = True)
    type = models.CharField(max_length = 100)

class Donor(User):
    name = models.CharField(max_length = 100)
    is_patient = models.BooleanField(default = False)
    location = models.ForeignKey(Location, null = True, blank = True)
    hospital = models.ForeignKey(Hospital, null = True)
    dob = models.DateField(null =  True)
    blood_group = models.CharField(max_length = 20, choices = blood_group_choices)
    is_alive = models.BooleanField(default = True)

class Organ(models.Model):
    type = models.CharField(max_length = 100, choices = organ_choices)
    donor = models.ForeignKey(Donor, null =  True, blank = True)
    receiver = models.ForeignKey(Donor, null = True, blank = True)
    blood_group = models.CharField(max_length = 20, choices = blood_group_choices)
    is_available = models.BooleanField(default =  True)
    hospital = models.ForeignKey(Hospital, null = True, blank = True)
