from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "time", "people", "created_date")
    list_filter = ("date", "time")
    search_fields = ("user__email", "user__username", "user__profile__phone")  # بستگی به مدل profile داره
    ordering = ("-created_date",)
    readonly_fields = ("created_date",)

    fieldsets = (
        (None, {
            "fields": ("user", "people")
        }),
        ("زمان رزرو", {
            "fields": ("date", "time")
        }),
        ("اطلاعات سیستمی", {
            "fields": ("created_date",)
        }),
    )
