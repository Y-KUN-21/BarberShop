from django.db import models


# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    preferred_time = models.CharField(max_length=250,default="10:00 - 12:00 PM")
    service = models.CharField(max_length=250)

    def __str__(self):
        return self.name