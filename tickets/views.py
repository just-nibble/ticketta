# from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Ticket
from .permissions import CanEditTicket
from .serializers import TIcketSerializer
# Create your views here.


class TicketAPIView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TIcketSerializer


class TickerDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CanEditTicket, )
    queryset = Ticket.objects.all()
    serializer_class = TIcketSerializer
