# Generated by Django 3.0 on 2022-03-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_auto_20220302_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='qrcode',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]