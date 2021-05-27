from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    phone = models.BigIntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)


class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    place = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name) + '-' + str(self.place)

    class Meta:
        verbose_name_plural = 'events'


class EventBooking(models.Model):
    user_name = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    event_place = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    event_time = models.DateTimeField(null=True, blank=True)
    amount = models.IntegerField()
    booking_time = models.DateTimeField()