from django.shortcuts import render
from django.views import View
from .models import Event, Attendee, Ticket,Venue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm,EventForm,TicketForm

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        now = timezone.now()
        past_month = now - timedelta(days=30)

        # Get basic metrics
        event_count = Event.objects.count()
        attendee_count = Attendee.objects.count()
        ticket_count = Ticket.objects.count()

        # Upcoming Events
        upcoming_events = Event.objects.filter(start_time__gte=now).order_by('start_time')[:5]

        # Recent Tickets
        recent_tickets = Ticket.objects.order_by('-created_at')[:5]

        # Events in the Past Month
        events_past_month_count = Event.objects.filter(start_time__gte=past_month).count()

        context = {
            'event_count': event_count,
            'attendee_count': attendee_count,
            'ticket_count': ticket_count,
            'upcoming_events': upcoming_events,
            'recent_tickets': recent_tickets,
            'events_past_month_count': events_past_month_count,
        }
        return render(request, 'dashboard.html', context)
    
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('user-list')

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

class UserUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user-list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list')

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')

class VenueListView(ListView):
    model = Venue
    template_name = 'venues/venue_list.html'
    context_object_name = 'venues'

class VenueDetailView(DetailView):
    model = Venue
    template_name = 'venues/venue_detail.html'
    context_object_name = 'venue'

class VenueCreateView(CreateView):
    model = Venue
    fields = ['name', 'address', 'capacity']
    template_name = 'venues/venue_form.html'
    success_url = reverse_lazy('venue-list')

class VenueUpdateView(UpdateView):
    model = Venue
    fields = ['name', 'address', 'capacity']
    template_name = 'venues/venue_form.html'
    success_url = reverse_lazy('venue-list')

class VenueDeleteView(DeleteView):
    model = Venue
    template_name = 'venues/venue_confirm_delete.html'
    success_url = reverse_lazy('venue-list')

class AttendeeListView(ListView):
    model = Attendee
    template_name = 'attendees/attendee_list.html'
    context_object_name = 'attendees'

class AttendeeCreateView(CreateView):
    model = Attendee
    fields = ['user', 'event']
    template_name = 'attendees/attendee_form.html'
    success_url = reverse_lazy('attendee-list')

class AttendeeUpdateView(UpdateView):
    model = Attendee
    fields = ['user', 'event', 'checked_in']
    template_name = 'attendees/attendee_form.html'
    success_url = reverse_lazy('attendee-list')

class AttendeeDeleteView(DeleteView):
    model = Attendee
    template_name = 'attendees/attendee_confirm_delete.html'
    success_url = reverse_lazy('attendee-list')

class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Debugging form fields
        print("Form fields:", form.fields)
        return form

class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket-list')

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'tickets/ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket-list')