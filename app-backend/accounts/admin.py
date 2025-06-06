# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth import get_user_model
# from .models import Profile

# CustomeUser = get_user_model()


# class CustomUserAdmin(UserAdmin):
#     """
#     Custom admin panel for user management with add and change forms plus password
#     """

#     model = CustomeUser
#     list_display = ("id","email", "is_superuser", "is_active", "is_verified")
#     list_filter = ("email", "is_superuser", "is_active", "is_verified")
#     searching_fields = ("email",)
#     ordering = ("email",)
#     fieldsets = (
#         (
#             "Authentication",
#             {
#                 "fields": ("email", "password"),
#             },
#         ),
#         (
#             "permissions",
#             {
#                 "fields": (
#                     "is_staff",
#                     "is_active",
#                     "is_superuser",
#                     "is_verified",
#                 ),
#             },
#         ),
#         (
#             "group permissions",
#             {
#                 "fields": ("groups", "user_permissions","type"),
#             },
#         ),
#         (
#             "important date",
#             {
#                 "fields": ("last_login",),
#             },
#         ),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "email",
#                     "password1",
#                     "password2",
#                     "is_staff",
#                     "is_active",
#                     "is_superuser",
#                     "is_verified",
#                     "type"
#                 ),
#             },
#         ),
#     )

# class CustomProfileAdmin(admin.ModelAdmin):
#     list_display = ("id","user", "first_name","last_name","phone_number")
#     searching_fields = ("user","first_name","last_name","phone_number")

# admin.site.register(CustomeUser, CustomUserAdmin)
# admin.site.register(Profile,CustomProfileAdmin)



