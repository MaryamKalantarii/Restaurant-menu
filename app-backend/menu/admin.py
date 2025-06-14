from django.contrib import admin
from .models import MenuItem, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)
    ordering = ("title",)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "stock", "status", "is_featured", "created_date")
    list_filter = ("status", "is_featured", "category")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("category",)
    readonly_fields = ("views", "created_date", "updated_date")
    fieldsets = (
        ("اطلاعات کلی", {
            "fields": ("title", "slug", "description", "category", "user")
        }),
        ("تصاویر", {
            "fields": ("image",)
        }),
        ("وضعیت و قیمت", {
            "fields": ("price", "discount_percent", "stock", "status", "is_featured")
        }),
        ("سایر", {
            "fields": ("views", "preparation_time", "created_date", "updated_date")
        }),
    )



