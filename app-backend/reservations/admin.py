from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "date", "time", "people", "created_at")
    list_filter = ("date", "time")
    search_fields = ("name", "email", "phone")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        (None, {
            "fields": ("name", "email", "phone", "people")
        }),
        ("زمان رزرو", {
            "fields": ("date", "time")
        }),
        ("اطلاعات سیستمی", {
            "fields": ("created_at",)
        }),
    )
