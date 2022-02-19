# Generated by Django 3.0 on 2022-02-19 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_url',
            field=models.URLField(blank=True, help_text='example: http://example.com', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='important_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Organizer',
        ),
    ]