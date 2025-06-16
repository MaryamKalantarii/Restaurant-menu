from rest_framework import serializers
from accounts.models import CustomeUser, Profile
from reservations.models import Reservation

class AdminReservationSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    class Meta:
        model = Reservation
        fields = ['id','user', 'user_email', 'date', 'time', 'people']

    def get_user_email(self, obj):
        return obj.user.email


from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Profile  # اگر پروفایل جداست

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number', 'image']

class AdminUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'is_active', 'is_staff', 'profile']

    def update(self, instance, validated_data):
        # آپدیت یوزر و پروفایل با هم
        profile_data = validated_data.pop('profile', {})
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        profile = instance.profile
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()

        return instance
