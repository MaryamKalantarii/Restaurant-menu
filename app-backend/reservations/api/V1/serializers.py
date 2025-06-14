from rest_framework import serializers
from reservations.models import Reservation
from datetime import datetime, time

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'name', 'date', 'time', 'people', 'email', 'phone']
        read_only_fields = ['id', 'email', 'phone']  # این دو تا فقط از سمت سرور تنظیم می‌شن

    def validate(self, data):
        if data['date'] < datetime.today().date():
            raise serializers.ValidationError("تاریخ رزرو نمی‌تواند در گذشته باشد.")
        
        if not time(12, 0) <= data['time'] <= time(22, 0):
            raise serializers.ValidationError("رزرو فقط بین ساعت 12 تا 22 ممکن است.")
        
        return data

    