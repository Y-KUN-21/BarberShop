from django import forms
import datetime
from dateutil.relativedelta import *

min_date = datetime.date.today()
max_date = min_date + relativedelta(weeks=+2)


class AppointmentForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="E-mail")
    preferred_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'type': 'date',
            'max': max_date,
            'min': min_date,
        })
    )
    preferred_time = forms.ChoiceField(
        choices=[('07:30 - 10:00 AM', "07:30 - 10:00 AM"), ('10:00 - 12:00 PM', "10:00 - 12:00 PM"),
                 ('12:00 - 14:00 PM', "12:00 - 14:00 PM"), ('14:00 - 16:00 PM', "14:00 - 16:00 PM"),
                 ('16:00 - 18:00 PM', "16:00 - 18:00 PM"), ('18:00 - 20:00 PM', "18:00 - 20:00 PM"),
                 ('20:00 - 22:30 PM', "20:00 - 22:30 PM"), ],
        label="Preferred time")
    service = forms.ChoiceField(choices=[('Haircut', "Haircut"), ('Shaving', "Shaving"),
                                         ('Color', "Color"), ('Face Massage', "Face Massage"),
                                         ('Face Scrub', "Face Scrub"), ('Facial', "Facial"), ('Clean up', "Clean up"),
                                         ("Head Massage", "Head Massage")], label="Appointment for")
