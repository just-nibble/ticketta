import qrcode

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# from django.core.mail import send_mail

from Ticketta.settings import MEDIA_ROOT

from tickets.models import Ticket
# Create your models here.

User = get_user_model()


class Purchase(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    ticket = models.ForeignKey(
        Ticket, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    used = models.BooleanField(default=False)
    qrcode = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ": " + self.ticket.event.event_title

    def save(self, *args, **kwargs):
        self.ticket.total = self.ticket.total - self.quantity
        self.ticket.save()
        increment = Purchase.objects.count() + 1
        destination = f"{MEDIA_ROOT}/qrcode/{self.user.username}_{self.ticket.event.event_title}{increment}.png"

        self.slug = slugify(self.user.username +
                            self.ticket.event.event_title + increment)
        # Generate QR code here

        self.url = f"https://test_url.com/purchases/{self.slug}"

        qrCode = qrcode.make(self.url)
        qrCode.save(destination)
        self.qrcode = f"http://127.0.0.1:8000/media/qrcode/{self.user.username}_{self.ticket.event.event_title}{increment}.png"

        # Upload QR code here

        # send_mail(qrcode="insert link" + self.ticket.ticket_number)

        super(Purchase, self).save(*args, **kwargs)
