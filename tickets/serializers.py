from rest_framework import serializers

from .models import Ticket


class TIcketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        read_only_fields = ("ticket_number", )
        fields = ("__all__")
