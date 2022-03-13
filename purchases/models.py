import qrcode

from io import BytesIO

import boto3

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.core.mail import send_mail

from django.db.models.signals import post_save
from django.dispatch import receiver

from djangoflutterwave.models import FlwPlanModel, FlwTransactionModel


from tickets.models import Ticket


from Ticketta.settings import (
    HOSTED, ALLOWED_HOSTS, AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY
)


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

            self.slug = slugify(self.user.username +
                                self.ticket.event.event_title + increment)
            # Generate QR code here

            self.url = f"{host}/purchases/{self.slug}"

            qrCode = qrcode.make(self.url)
            buffer = BytesIO()
            qrCode.save(buffer, "PNG")
            s3 = boto3.client('s3')
            s3 = boto3.client(
                's3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                region_name='eu-west-3'
            )
            s3.put_object(
                Bucket='mint-engine',
                Key='purchases/qrcode/'+self.user.username+"_" +
                    self.ticket.event.event_title+increment+'.png',
                Body=buffer,
                ContentType='image/png',
            )
            self.qrCode = f"""https://mint-engine.s3.eu-west-3.amazonaws.com/purchases/qrcode/{self.user.username}_{self.ticket.event.event_title}{increment}.png
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


@receiver(post_save, sender=FlwTransactionModel)
def set_paid(sender, instance, *args, **kwargs):
    plan = instance.plan
    purchase = Purchase.objects.get(plan=plan)
    purchase.status = "paid"
    purchase.save()
