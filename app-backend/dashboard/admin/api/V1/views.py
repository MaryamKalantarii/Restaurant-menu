from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from accounts.models import CustomeUser
from reservations.models import Reservation
from .serializers import CustomeUserSerializer
from reservations.api.V1.serializers import ReservationSerializer

class AdminUserViewSet(ModelViewSet):
    queryset = CustomeUser.objects.select_related('user_profile').all()
    serializer_class = CustomeUserSerializer
    permission_classes = [IsAdminUser]

class AdminReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.select_related('user').all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAdminUser]