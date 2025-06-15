from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservation_user")
    date = models.DateField(verbose_name="روز")
    time = models.TimeField(verbose_name="زمان")
    people = models.PositiveIntegerField(verbose_name="تعداد")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "رزرو میز"

    def __str__(self):
        return f"{self.user.email} - {self.date} {self.time}"

