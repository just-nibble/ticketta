from __future__ import unicode_literals

from django.db import models
from accounts.models import CustomUser as User


Transaction_Type = (
    ('send', 'Send'),
    ('request', 'Request'),
    ('transfer', 'Transfer'),
)


class Wallet(models.Model):
    # We should reference to the AUTH_USER_MODEL so that
    # when this module is used and a different User is used,
    # this would still work out of the box.
    #
    # See 'Referencing the User model' [1]
    wallet_address = models.UUIDField(unique=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    # This stores the wallet's current balance. Also acts
    # like a cache to the wallet's balance as well.
    current_balance = models.FloatField(default=0.00)

    # The date/time of the creation of this wallet.
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user.email)

    def can_send(self, amount):
        return (self.current_balance - amount) >= 0

    def sum(self, amount):
        self.current_balance += amount
        return self.save()

    def remove(self, amount):
        self.current_balance -= amount
        return self.save()


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(
        max_length=45, choices=Transaction_Type, default='')
    previous_amount = models.FloatField(default=0.00)
    current_amount = models.FloatField(default=0.00)
    create_date = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=60, default='pending', blank=True)
    receiver = models.ForeignKey(
        Wallet, related_name='receiver', on_delete=models.PROTECT, default='')
    creator = models.ForeignKey(
        Wallet, related_name='creator', on_delete=models.PROTECT, default='')

    def __str__(self):
        return str(self.transaction_id)

    def save(self, *args, **kwargs):

        has_enough_money = self.creator.can_send(self.amount)

        if not has_enough_money:
            return {
                'error': 'Owner wallet must have enough money'
            }
        elif self.amount <= 0:
            return {
                'error': 'Amount must be positive',
            }
        else:
            #  Update the amount of the wallets
            self.creator.remove(self.amount)
            self.receiver.sum(self.amount)

            return super(Transaction, self).save(*args, **kwargs)
