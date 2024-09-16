from django import forms
from django.contrib.auth.models import User
from .models import *

class CustomUserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'venue', 'start_time', 'end_time', 'organizer', 'max_attendees']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organizer'].queryset = User.objects.all()

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'attendee', 'ticket_type', 'price']
        widgets = {
            'event': forms.Select(),  # Using default Select widget for event
            'attendee': forms.Select(),  # Using default Select widget for attendee
        }
