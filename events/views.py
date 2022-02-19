# from django.shortcuts import render

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Event
from . permissions import CanEditEvent
from .serializers import EventSerializer
# Create your views here.


class EventListCreateAPIView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CanEditEvent, )
    serializer_class = EventSerializer
    queryset = Event.objects.all()
