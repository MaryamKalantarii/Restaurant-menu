from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from reservations.models import Reservation
from rest_framework import permissions
from reservations.models import Reservation
from .serializers import AdminReservationSerializer,AdminUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class AdminReservationCreateView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = AdminReservationSerializer
    permission_classes = [IsAdminUser]



class AdminUserViewSet(ModelViewSet):
    queryset = User.objects.all().select_related('profile')
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]


