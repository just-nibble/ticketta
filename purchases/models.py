from django.db import models
from django.contrib.auth import get_user_model

from tickets.models import Ticket
# Create your models here.

User = get_user_model()


class Purchase(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    ticket = models.ForeignKey(
        Ticket, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ": " + self.ticket.event.name

    def save(self, *args, **kwargs):
        self.ticket.total = self.ticket.total - self.quantity
        self.ticket.save()
