# python import
import random

from django.db import models
from django.contrib.auth import get_user_model

from events.models import Event

User = get_user_model()
# Create your models here.


class Ticket(models.Model):
    ticket_status_choices = (
        ('pending', 'pending'), ('on sale', 'on sale'),
        ('sold out', 'sold out'),
    )

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    ticket_number = models.IntegerField(null=True, blank=True, unique=True)
    ticket_type = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=255, null=True, blank=True, choices=ticket_status_choices)

    def __str__(self):
        return self.event.event_title

    def generateTicketNumber(self):
        self.ticket_number = random.randint(1000, 1000000000)

    def save(self, *args, **kwargs):
        self.generateTicketNumber()
        super(Ticket, self).save(*args, **kwargs)
