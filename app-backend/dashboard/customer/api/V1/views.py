from rest_framework import generics, permissions
from django.http import Http404
from accounts.models import Profile
from reservations.models import Reservation
from dashboard.customer.api.V1.serializers import UpdateProfileCustomerSerializer, GetProfileCustomerSerializer, \
                                    CustomerReservationSerializer



class UpdateProfileCustomerAPIView(generics.UpdateAPIView):

    """Update the authenticated user's profile."""

    serializer_class = UpdateProfileCustomerSerializer
    queryset = Profile.objects.select_related("user")
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return self.queryset.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise Http404("پروفایل کاربر یافت نشد")


class GetProfileCustomerAPIView(generics.RetrieveAPIView):

    """Retrieve the profile of the authenticated user."""

    queryset = Profile.objects.select_related("user")
    serializer_class = GetProfileCustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return self.queryset.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise Http404("پروفایل کاربر یافت نشد")
        


class GetReservationCustomerListAPIView(generics.ListAPIView):
    serializer_class = CustomerReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
    