from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib import messages
from .models import Appointment


# Create your views here.
def home(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            preferred_time = form.cleaned_data['preferred_time']
            service = form.cleaned_data['service']
            # instance = Appointment(name=name, email=email, preferred_time=preferred_time, service=service)
            # instance.save()

            messages.success(request, 'Appointment placed successfully')
            print("Saved")
        return render(request, "barbershop/home.html", {"form": form})
    form = AppointmentForm()
    return render(request, "barbershop/home.html", {"form": form})


def confirmed(request):
    return render(request, "barbershop/confirmed.html")
