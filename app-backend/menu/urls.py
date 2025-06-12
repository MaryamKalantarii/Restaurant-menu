from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('items', views.MenuViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = router.urls