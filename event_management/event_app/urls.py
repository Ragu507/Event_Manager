from django.urls import path
from .views import (
    DashboardView,
    EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    AttendeeListView, AttendeeCreateView, AttendeeUpdateView, AttendeeDeleteView,
    TicketListView, TicketCreateView, TicketUpdateView, TicketDeleteView,
    VenueListView, VenueDetailView, VenueCreateView, VenueUpdateView, VenueDeleteView, RegisterView, UserListView, UserUpdateView, UserDeleteView, UserDetailView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),

    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

    # Event URLs
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/create/', EventCreateView.as_view(), name='event-create'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

    # Attendee URLs
    path('attendees/', AttendeeListView.as_view(), name='attendee-list'),
    # path('attendees/<int:pk>/', AttendeeDetailView.as_view(), name='attendee-detail'),
    path('attendees/create/', AttendeeCreateView.as_view(), name='attendee-create'),
    path('attendees/<int:pk>/update/', AttendeeUpdateView.as_view(), name='attendee-update'),
    path('attendees/<int:pk>/delete/', AttendeeDeleteView.as_view(), name='attendee-delete'),

    # Ticket URLs
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    # path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('tickets/<int:pk>/update/', TicketUpdateView.as_view(), name='ticket-update'),
    path('tickets/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket-delete'),

    # Venue URLs
    path('venues/', VenueListView.as_view(), name='venue-list'),
    path('venues/<int:pk>/', VenueDetailView.as_view(), name='venue-detail'),
    path('venues/create/', VenueCreateView.as_view(), name='venue-create'),
    path('venues/<int:pk>/update/', VenueUpdateView.as_view(), name='venue-update'),
    path('venues/<int:pk>/delete/', VenueDeleteView.as_view(), name='venue-delete'),
]
