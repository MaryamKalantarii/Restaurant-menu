from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Profile
from reservations.models import Reservation
from dashboard.admin.api.V1.serializers import GetUserSerializer


User = get_user_model()



class UpdateProfileCustomerSerializer(serializers.ModelSerializer):
    user = GetUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "first_name", "last_name", "image", "phone_number"]


class GetProfileCustomerSerializer(serializers.ModelSerializer):
    user = GetUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "first_name", "last_name", "phone_number", "image", "created_date", "updated_date"]


class CustomerReservationSerializer(serializers.ModelSerializer):
    user = GetUserSerializer(read_only=True)
    
    class Meta:
        model = Reservation
        fields = '__all__'
