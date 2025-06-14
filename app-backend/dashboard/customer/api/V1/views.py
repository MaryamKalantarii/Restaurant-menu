from rest_framework.generics import RetrieveUpdateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from reservations.models import Reservation
from dashboard.admin.api.V1.serializers import (
        ProfileSerializer
)
from reservations.api.V1.serializers import ReservationSerializer

class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.user_profile

class ReservationCustomerListAPIView(ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
    