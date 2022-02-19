from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Event(models.Model):
    event_title = models.CharField(max_length=255, null=True, blank=True)
    start_date_time = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    end_date_time = models.DateTimeField(null=True, blank=True)
    venue = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    important_notes = models.TextField(null=True, blank=True)
    income = models.IntegerField(null=True, blank=True)
    event_url = models.URLField(
        null=True, blank=True, help_text="example: http://example.com")
    organizer = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_title
