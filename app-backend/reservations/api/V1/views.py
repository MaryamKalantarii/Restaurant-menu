from rest_framework import generics
from ...models import Reservation
from .serializers import ReservationSerializer
from rest_framework.permissions import IsAuthenticated

# from email import send_reservation_email

class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        reservation = serializer.save()
        # send_reservation_email(reservation)


class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]