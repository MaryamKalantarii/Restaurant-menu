from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from reservations.models import Reservation
from .serializers import ReservationSerializer
from .tasks import send_reservation_email  # اگه ایمیل رو با Celery می‌فرستی
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class ReservationCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.select_related("user")

    def perform_create(self, serializer):
        user = self.request.user

        try:
            phone = user.profile.phone_number
        except AttributeError:
            raise ValidationError("پروفایل شما کامل نیست. لطفاً شماره تلفن خود را در پروفایل وارد کنید.")

        if not phone:
            raise ValidationError("شماره تلفن شما ثبت نشده. لطفاً ابتدا پروفایل خود را تکمیل کنید.")

        reservation = serializer.save(user=user)

        # ارسال ایمیل
        try:
            name = user.profile.get_fullname() if hasattr(user, "profile") else user.username

            send_reservation_email.delay(
                name,
                user.email,
                str(reservation.date),
                str(reservation.time)
            )
        except Exception as e:
            print(f"Error sending reservation email: {e}")





class MyReservationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reservations = Reservation.objects.filter(user=request.user)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
