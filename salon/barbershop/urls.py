from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('appointment/', views.appointment, name="appointment"),
    path('appointment_list/', views.appointments_list, name="appointments_list")
]