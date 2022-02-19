# from django.shortcuts import render
# RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView
from .serializers import PurchaseSerializer
from .models import Purchase

# Create your views here.


class PurchaseAPIView(ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def perform_create(self, serializer, **kwargs):
        current_user = self.request.user
        kwargs['user'] = current_user
        serializer.save(**kwargs)
