# Generated by Django 2.0.8 on 2018-08-13 15:54

from django.db import migrations, models
import safe_relay_service.safe.safe_service


class Migration(migrations.Migration):

    dependencies = [
        ('safe', '0009_auto_20180810_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safemultisigtx',
            name='operation',
            field=models.PositiveSmallIntegerField(choices=[(safe_relay_service.safe.safe_service.SafeOperation(0), 0), (safe_relay_service.safe.safe_service.SafeOperation(1), 1), (safe_relay_service.safe.safe_service.SafeOperation(2), 2)]),
        ),
    ]