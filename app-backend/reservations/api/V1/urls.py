from django.urls import path
from .views import ReservationCreateView,ReservationListView


app_name = 'reserv-api'

urlpatterns = [
    path('reserve/', ReservationCreateView.as_view(), name='reserve'),
    path('reserve-list/', ReservationListView.as_view(), name='reserve-list'),
]
