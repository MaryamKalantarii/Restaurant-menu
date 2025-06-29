from django.urls import path
from .views import ReservationCreateView
from .views import MyReservationsView

app_name = 'reserv-api'

urlpatterns = [
    path('reserve/', ReservationCreateView.as_view(), name='reserve'),
    path('user-reservations/', MyReservationsView.as_view(), name='user_reservations'),
]
