from rest_framework import serializers
from .models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("user", "current_balance", "created_at")


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("__all__")


class WithdrawalSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
