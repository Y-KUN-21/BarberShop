# Generated by Django 3.1.3 on 2020-11-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0003_remove_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='preferred_time',
            field=models.CharField(default='10:00 - 12:00 PM', max_length=250),
        ),
    ]
