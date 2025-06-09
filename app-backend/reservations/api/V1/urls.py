from django.urls import path
from .views import ReservationCreateView,AdminReservationListView, \
                    GetReservationCustomerListAPIView, DeleteResevationAPIView


app_name = 'reserv-api'

urlpatterns = [
    path('reserve/', ReservationCreateView.as_view(), name='reserve'),
    path('reserve-list_admin/', AdminReservationListView.as_view(), name='reserve-list-admin'),
    path('delete-reserve/<int:pk>/', DeleteResevationAPIView.as_view(), name='delete-reserve'),
    path('reserve-list_customer/', GetReservationCustomerListAPIView.as_view(), name='reserve-list-customer'),
]
