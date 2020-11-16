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
        choices=[('10:00-12:00 PM', "10:00 -12:00 PM"), ('12:00 - 14:00 PM', "12:00 - 14:00 PM"),
                 ('14:00 - 16:00 PM', "14:00 - 16:00 PM"), ('16:00 - 18:00 PM', "16:00 - 18:00 PM"),
                 ('18:00 - 20:00 PM', "18:00 - 20:00 PM"), ('20:00 - 22:00 PM', "20:00 - 22:00 PM"), ],
        label="Preferred time")
    service = forms.ChoiceField(choices=[('haircut', "Haircut"), ('shaving', "Shaving"),
                                         ('color', "color"), ('face_massage', "Face Massage( 15 mins )"),
                                         ('face_scrub', "Face Scrub"), ('facial', "Facial"), ('clean_up', "Clean up"),
                                         ("head_massage", "Head Massage")], label="Appointment for")
