import qrcode

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.mail import send_mail

from djangoflutterwave.models import FlwPlanModel


from tickets.models import Ticket


from Ticketta.settings import MEDIA_ROOT, HOSTED, ALLOWED_HOSTS


# Create your models here.

User = get_user_model()


class Purchase(models.Model):

    purchase_status = (("pending", "pending"),
                       ("paid", "paid"), ("used", "used"))
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    ticket = models.ForeignKey(
        Ticket, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=300, default="pending", blank=True)
    qrCode = models.CharField(max_length=300, null=True, blank=True)
    plan = models.ForeignKey(FlwPlanModel, null=True,
                             blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ": " + self.ticket.event.event_title

    def save(self, *args, **kwargs):
        if self.status == "paid":
            saleAmount = self.quantity * self.ticket.price
            sellerWallet = self.ticket.event.user
            sellerWallet.deposit(saleAmount)
            sellerWallet.save()

            if HOSTED:
                host = ALLOWED_HOSTS[0] + ":8000"
            else:
                host = ALLOWED_HOSTS[2]

            self.ticket.total = self.ticket.total - \
                (saleAmount/self.ticket.price)
            self.ticket.save()
            increment = Purchase.objects.count() + 1
            destination = f"""
            {MEDIA_ROOT}/qrcode/{self.user.username}_{self.ticket.event.event_title}{increment}.png
            """

            self.slug = slugify(self.user.username +
                                self.ticket.event.event_title + increment)
            # Generate QR code here

            self.url = f"{host}/purchases/{self.slug}"

            qrCode = qrcode.make(self.url)
            qrCode.save(destination)
            self.qrcode = f"""
            {host}/media/qrcode/{self.user.username}_{self.ticket.event.event_title}{increment}.png
            """

            recipient_list = [self.user.email, ]
            send_mail(
                "Ticket Purchase",
                f"""
                You have purchased {self.quantity} tickets for the event:
                {self.ticket.event.event_title}, below is a link to the ticket
                and a link to it's QRcode

                link: {self.url}
                qrcode: {self.qrcode}

                """,
                "ticketta@gmail.com", recipient_list, fail_silently=False
            )
        elif self.status == "pending":
            plan = FlwPlanModel(
                name=self.ticket.ticket_number,
                amount=saleAmount,
                modal_title=self.ticket.event.event_title,

            )
            plan.save()
            self.plan = plan

        super(Purchase, self).save(*args, **kwargs)
