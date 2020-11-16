from django.db import models
import datetime


# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    preferred_date = models.DateField(default=datetime.date.today)
    preferred_time = models.CharField(max_length=250, default="10:00 - 12:00 PM")
    service = models.CharField(max_length=250)
    appointment_id = models.CharField(max_length=450)

    def __str__(self):
        return self.name
