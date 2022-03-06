# from django.shortcuts import render
from rest_framework import generics
# from rest_framework.views import APIView
from .models import (
    Wallet, Transaction
)
from .serializers import WalletSerializer, TransactionSerializer


# Create your views here.


class WalletList(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class Transfer(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()

    serializer_class = TransactionSerializer


class Deposit(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = WalletSerializer
