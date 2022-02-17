# Generated by Django 3.2.12 on 2022-02-17 06:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='rental_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cart',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 18, 6, 31, 12, 696454, tzinfo=utc)),
        ),
    ]