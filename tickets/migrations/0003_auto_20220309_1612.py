# Generated by Django 3.0 on 2022-03-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20220219_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_number',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
