# reservations/serializers.py
from rest_framework import serializers
from ...models import Reservation
from datetime import datetime, time

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        # بررسی تاریخ گذشته
        if data['date'] < datetime.today().date():
            raise serializers.ValidationError("تاریخ رزرو نمی‌تواند در گذشته باشد.")
        
        # بررسی ساعت کاری (مثلاً 12:00 تا 22:00)
        if not time(12, 0) <= data['time'] <= time(22, 0):
            raise serializers.ValidationError("رزرو فقط بین ساعت 12 تا 22 ممکن است.")
        
        return data