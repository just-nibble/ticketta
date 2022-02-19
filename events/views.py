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

    def perform_create(self, serializer, **kwargs):
        current_user = self.request.user
        kwargs['organizer'] = current_user
        serializer.save(**kwargs)


class EventDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CanEditEvent, )
    serializer_class = EventSerializer
    queryset = Event.objects.all()
