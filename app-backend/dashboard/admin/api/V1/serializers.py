from rest_framework import serializers
from accounts.models import CustomeUser, Profile
from reservations.models import Reservation
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'image', 'phone_number', 'created_date', 'updated_date']

class CustomeUserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer()

    class Meta:
        model = CustomeUser
        fields = ['id', 'email', 'is_active', 'is_staff', 'is_superuser',
                  'is_verified', 'type', 'created_date', 'updated_date', 'user_profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('user_profile')
        user = CustomeUser.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('user_profile', None)
        user = super().update(instance, validated_data)

        if profile_data:
            profile = user.user_profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()

        return user

class AdminReservationSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    class Meta:
        model = Reservation
        fields = ['id','user', 'user_email', 'date', 'time', 'people']

    def get_user_email(self, obj):
        return obj.user.email