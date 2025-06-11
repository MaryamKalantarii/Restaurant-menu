from django.urls import path
from .views import ReservationCreateView


app_name = 'reserv-api'

urlpatterns = [
    path('reserve/', ReservationCreateView.as_view(), name='reserve'),
]
