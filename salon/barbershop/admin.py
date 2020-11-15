from django.contrib import admin
from .models import Appointment

# Register your models here.
admin.site.site_header = "Appointments panel"
admin.site.register(Appointment)
