from django.urls import path, re_path
from .views import *


app_name = 'api-v1-menu'

urlpatterns = [
    path("all_menu/", GetListItemMenuAPIView.as_view(), name="all_menu"),
    re_path(r'^(?P<slug>[-\wآ-ی]+)/get_menu/', GetItemMenuAPIView.as_view(), name='get_menu'),
    path("all_category/", GetListCategoryMenuAPIView.as_view(), name="all_category"),
    re_path(r'^(?P<slug>[-\wآ-ی]+)/get_category/', GetCategoryMenuAPIView.as_view(), name='get_category'),
]
