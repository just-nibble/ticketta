from django.db import models

# Create your models here.


class Event(models.Model):
    event_title = models.CharField(max_length=255, null=True, blank=True)
    start_date_time = models.DateTimeField(null=True, blank=True)
    end_date_time = models.DateTimeField(null=True, blank=True)
    venue = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    important_notes = models.CharField(max_length=255, null=True, blank=True)
    income = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.event_title


class Organizer(models.Model):
    event = models.ForeignKey(
        Event, null=True, blank=True, on_delete=models.CASCADE)
