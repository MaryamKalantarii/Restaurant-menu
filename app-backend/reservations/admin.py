from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "date", "time", "people", "created_date")
    list_filter = ("date", "time")
    search_fields = ("name", "email", "phone")
    ordering = ("-created_date",)
    readonly_fields = ("created_date",)

    fieldsets = (
        (None, {
            "fields": ("name", "email", "phone", "people")
        }),
        ("زمان رزرو", {
            "fields": ("date", "time")
        }),
        ("اطلاعات سیستمی", {
            "fields": ("created_date",)
        }),
    )
