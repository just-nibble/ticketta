# from django.shortcuts import render
# RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class PurchaseUseAPIView(APIView):
    def get(self, request, slug):
        purchase = Purchase.objects.get(slug=slug)

        if purchase.used:
            raise ValidationError({"error": "Ticket has already been used"})
        else:
            return Response(
                {
                    "id": purchase.id,
                    "slug": purchase.slug,
                    "user__first_name": purchase.user.first_name,
                    "user__last_name": purchase.user.last_name,
                    "user__email": purchase.user.email,
                    "ticket_number": purchase.ticket.ticket_number,
                    "ticket_type": purchase.ticket.ticket_type,
                    "ticket_status": purchase.ticket.status,
                    "ticket_quantity": purchase.ticket.quantity,
                }
            )
