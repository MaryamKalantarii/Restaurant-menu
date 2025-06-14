from rest_framework import generics
from reservations.models import Reservation  
from .serializers import ReservationSerializer
from reservations.api.V1.tasks import send_reservation_email  
from rest_framework.permissions import IsAuthenticated



from rest_framework.exceptions import ValidationError

class ReservationCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.select_related("user")
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        user = self.request.user

        # بررسی اینکه پروفایل کاربر شماره تلفن داره یا نه
        try:
            phone = user.profile.phone
        except AttributeError:
            raise ValidationError("پروفایل شما کامل نیست. لطفاً شماره تلفن خود را در پروفایل وارد کنید.")

        if not phone:
            raise ValidationError("شماره تلفن یافت نشد. لطفاً پروفایل خود را کامل کنید.")

        # ذخیره رزرو با ایمیل و تلفن از اطلاعات کاربر
        reservation = serializer.save(
            user=user,
            email=user.email,
            phone=phone
        )

        # ارسال ایمیل
        try:
            send_reservation_email.delay(
                reservation.name,
                reservation.email,
                str(reservation.date),
                str(reservation.time)
            )
        except Exception as e:
            print(f"Error sending reservation email: {e}")
