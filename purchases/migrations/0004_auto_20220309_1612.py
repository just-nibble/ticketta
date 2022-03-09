# Generated by Django 3.0 on 2022-03-09 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoflutterwave', '0002_auto_20201222_0800'),
        ('purchases', '0003_purchase_qrcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='qrcode',
            new_name='qrCode',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='used',
        ),
        migrations.AddField(
            model_name='purchase',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoflutterwave.FlwPlanModel'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=300),
        ),
    ]
