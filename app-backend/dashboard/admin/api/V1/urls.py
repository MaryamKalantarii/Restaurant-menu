from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminUserViewSet,AdminReservationCreateView

router = DefaultRouter()
router.register('admin/users', AdminUserViewSet, basename='admin-users'),
router.register('admin/reservation', AdminReservationCreateView, basename='reservation')

urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('admin/reservations/create/', AdminReservationCreateView.as_view(), name='admin-reservation-create'),
# ]



