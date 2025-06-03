from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=15,verbose_name="شماره تلفن")
    date = models.DateField(verbose_name="روز")
    time = models.TimeField(verbose_name="زمان")
    people = models.PositiveIntegerField(verbose_name="تعداد")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ساخت")

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "رزرو میز"
    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
