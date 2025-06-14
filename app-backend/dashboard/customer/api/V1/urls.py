from django.urls import path
from .views import UserProfileView,ReservationCustomerListAPIView

urlpatterns = [
    path('my-profile/', UserProfileView.as_view(), name='my-profile'),
    path('my-reserved/', ReservationCustomerListAPIView.as_view(), name='List-reserved'),
]