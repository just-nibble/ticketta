# from django.shortcuts import render
from rest_framework import renderers
from rest_framework.views import APIView
from .models import (
    Wallet, Withdrawal
)
from .serializers import WithdrawalSerializer


# Create your views here.


class WithdrawalAPIView(APIView):
    serializer_class = WithdrawalSerializer
    renderer_classes = (
        renderers.BrowsableAPIRenderer, renderers.JSONRenderer,
        renderers.HTMLFormRenderer, renderers.DocumentationRenderer
    )

    def post(self, request):
        serializer = WithdrawalSerializer(
            data=request.data)

        currentUser = request.user
        wallet = Wallet.objects.get(user=currentUser)

        if serializer.is_valid(self):
            amount = serializer.validated_data.get("amount")

            canWithdraw = wallet.can_withdraw(amount)

            if canWithdraw:
                previousAmount = wallet.current_balance
                currentAmount = wallet.current_balance + amount
                withdrawal = Withdrawal(
                    creator=currentUser,
                    withdrawal_amount=amount,
                    previous_amount=previousAmount,
                    current_amount=currentAmount
                )
                withdrawal.save()

                wallet.withdraw(amount)
                wallet.save()

            else:
                raise serializer.ValidationError(
                    {"error": "Insufficient Balance"})
