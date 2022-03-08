from __future__ import unicode_literals

from django.core.mail import send_mail
from django.db import models
from accounts.models import CustomUser as User


Transaction_Type = (
    ('send', 'Send'),
    ('request', 'Request'),
    ('transfer', 'Transfer'),
)


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    # This stores the wallet's current balance. Also acts
    # like a cache to the wallet's balance as well.
    current_balance = models.PositiveIntegerField(default=0)
    bank_account_name = models.CharField(max_length=300, null=True, blank=True)
    bank_account_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user.email)

    def can_withdraw(self, amount):
        return (self.current_balance - amount) >= 0

    def deposit(self, amount):
        self.current_balance += amount
        return self.save()

    def withdraw(self, amount):
        self.current_balance -= amount
        return self.save()


class Withdrawal(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    previous_amount = models.PositiveIntegerField(default=0)
    current_amount = models.PositiveIntegerField(default=0)
    withdrawal_amout = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True, editable=False)
    creator = models.ForeignKey(
        Wallet, related_name='creator', on_delete=models.PROTECT, default='')

    def __str__(self):
        return str(self.transaction_id)

    def save(self, *args, **kwargs):
        send_mail(
            "Withdrawal Request",
            f"""
            You have made a withdrawal request for {self.withdrawal_amout},
            you will receive your requested amount at
            {self.creator.bank_account_name},
            with {self.creator.bank_account_number}.
            """,
            "ticketta.com",
            [self.creator.email]
        )
        return super(Wallet, self).save(*args, **kwargs)
