from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from accounts.models import CustomeUser
from reservations.models import Reservation
from .serializers import CustomeUserSerializer
from rest_framework import generics, permissions
from reservations.models import Reservation
from .serializers import AdminReservationSerializer

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class AdminReservationCreateView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = AdminReservationSerializer
    permission_classes = [IsAdminUser]

class AdminUserViewSet(ModelViewSet):
    queryset = CustomeUser.objects.select_related('user_profile').all()
    serializer_class = CustomeUserSerializer
    permission_classes = [IsAdminUser]

