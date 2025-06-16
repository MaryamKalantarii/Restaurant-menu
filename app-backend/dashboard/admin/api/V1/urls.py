from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('admin/reservation', AdminReservationCreateView, basename='reservation')
router.register('admin/users', AdminUserViewSet, basename='admin-users')
router.register('admin/menu', AdminMenuItemView, basename='admin-menu') 
router.register('admin/categories', AdminCategoryView, basename='admin-categories')
urlpatterns = router.urls



   

