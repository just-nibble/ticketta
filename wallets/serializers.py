from rest_framework import serializers
from .models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("user", "current_balance", "created_at")


class TransactionSerializer(serializers.ModelSerializer):
    creator = WalletSerializer(many=False)
    receiver = WalletSerializer(many=False)

    def create(self, validated_data):
        creator = Wallet.objects.get(user=validated_data['creator']['user'])
        receiver = Wallet.objects.get(user=validated_data['receiver']['user'])
        amount = validated_data['amount']
        transac = Transaction(
            receiver=receiver,
            creator=creator,
            amount=amount
        )
        search_error = transac.save()
        try:
            search_error = search_error.get('error', None)
        except Exception:
            return transac
        else:
            if search_error:
                raise serializers.ValidationError({'detail': search_error})

    class Meta:
        model = Transaction
        fields = ("__all__")
