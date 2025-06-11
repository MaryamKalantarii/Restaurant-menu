from django.urls import path, include



urlpatterns = [
    path("", include("dashboard.admin.api.V1.urls")),
    path("", include("dashboard.customer.api.V1.urls")),
]
