from rest_framework import generics
from reservations.models import Reservation  # دقت کنید که مسیر صحیح مدل رزرو را وارد کرده‌اید
from .serializers import ReservationSerializer
from reservations.api.V1.tasks import send_reservation_email  # وارد کردن تسک به مسیر صحیح



class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.select_related("user")
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        reservation = serializer.save(user=self.request.user)
        try:
            # ارسال ایمیل به صورت Async با Celery
            send_reservation_email.delay(
                reservation.name,
                reservation.email,
                str(reservation.date),
                str(reservation.time)
            )
        except Exception as e:
            # در صورت بروز مشکل می‌تونی پیام خطا رو چاپ کنی یا ذخیره کنی
            print(f"Error sending reservation email: {e}")
