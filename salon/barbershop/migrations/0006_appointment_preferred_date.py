# Generated by Django 3.1.3 on 2020-11-16 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0005_remove_appointment_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='preferred_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]