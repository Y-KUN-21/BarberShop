from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib import messages
from datetime import date, timedelta
from .models import Appointment


# Create your views here.
def home(request):
    return render(request, "barbershop/home.html")


def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            preferred_time = form.cleaned_data['preferred_time']
            service = form.cleaned_data['service']
            preferred_date = form.cleaned_data['preferred_date']
            appointment_id = name + "@" + email + "@" + str(preferred_date.strftime("%d-%m-%Y"))
            try:
                have_appointment = Appointment.objects.get(appointment_id=appointment_id)
                messages.success(request, '''Hey, {} you already have an appointment for "{}"on  {} between {}.'''.
                                 format(have_appointment.name, have_appointment.service,
                                        have_appointment.preferred_date.strftime("%d-%m-%Y"),
                                        have_appointment.preferred_time))
            except Appointment.DoesNotExist:
                instance = Appointment(name=name, email=email, preferred_time=preferred_time,
                                       preferred_date=preferred_date, service=service, appointment_id=appointment_id)
                instance.save()
                messages.info(request, "Take a screenshot of the below message please !")
                messages.success(request, '''Hey, {} you already have an appointment for "{}"on  {} between {} placed 
                successfully.'''.
                                 format(name, service, preferred_date.strftime("%d-%m-%Y"), preferred_time))
        return render(request, "barbershop/appointment.html", {"form": form})
    form = AppointmentForm()
    return render(request, "barbershop/appointment.html", {"form": form})


@login_required()
def appointments_list(request):
    today = date.today()
    seven_day = today + timedelta(days=6)
    month = today + timedelta(days=30)
    today_appointments = Appointment.objects.filter(preferred_date__range=[today, today])
    week_appointments = Appointment.objects.filter(preferred_date__range=[today, seven_day])
    month_appointments = Appointment.objects.filter(preferred_date__range=[today, month])
    return render(request, "barbershop/appointments_list.html", {"today_appointments": today_appointments,
                                                                 "week_appointments": week_appointments,
                                                                 "month_appointments": month_appointments, })
