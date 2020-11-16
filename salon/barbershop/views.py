from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib import messages
import datetime
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
            # instance = Appointment(name=name, email=email, preferred_time=preferred_time,
            # preferred_date=preferred_date, service=service) instance.save()
            messages.info(request, "Screenshot this message please !")
            messages.success(request, '''Hey, {} your appointment for "{}"
                                         on  {} between {} placed successfully.
                                         '''.
                             format(name, service, preferred_date.strftime("%d-%m-%Y"), preferred_time))
            print(name, email, preferred_date, preferred_time, service)
        return render(request, "barbershop/appointment.html", {"form": form})
    form = AppointmentForm()
    return render(request, "barbershop/appointment.html", {"form": form})
