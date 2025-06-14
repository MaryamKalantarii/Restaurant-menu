from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminUserViewSet,AdminReservationViewSet

router = DefaultRouter()
router.register('admin/users', AdminUserViewSet, basename='admin-users'),
router.register('admin/reservation', AdminReservationViewSet, basename='reservation')

urlpatterns = router.urls