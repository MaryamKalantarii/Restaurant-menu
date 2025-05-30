from django.urls import path, include
from .views import *  
from rest_framework.routers import DefaultRouter

app_name = 'api-v1-menu'

router = DefaultRouter()
router.register('menu-items', MenuItemView, basename='menu-items') 
router.register('categories', CategoryView, basename='categories')

urlpatterns = router.urls
