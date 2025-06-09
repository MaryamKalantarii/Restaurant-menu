from django.urls import path, re_path
from .views import *


app_name = 'api-v1-menu'

urlpatterns = [
    path("create_menu/", CreateMenuItemAPIView.as_view(), name="create_menu"),
    path("all_menu/", GetListItemMenuAPIView.as_view(), name="all_menu"),
    re_path(r'^(?P<slug>[-\wآ-ی]+)/get_menu/', GetItemMenuAPIView.as_view(), name='get_menu'),
    path("update_menu/<int:pk>/", UpdateMenuAPIView.as_view(), name="update_menu"),
    path("remove_menu/<int:pk>/", RemoveMenuAPIView.as_view(), name="remove_menu"),
    path("create_category/", CreateCategoryMenuAPIView.as_view(), name="create_category_menu"),
    path("all_category/", GetListCategoryMenuAPIView.as_view(), name="remove_menu"),
    re_path(r'^(?P<slug>[-\wآ-ی]+)/get_category/', GetCategoryMenuAPIView.as_view(), name='get_category'),
    path("update_category/<int:pk>/", UpdateCategoryMenuAPIView.as_view(), name="update_category"),
    path("remove_category/<int:pk>/", RemoveCategoryMenuAPIView.as_view(), name="remove_category"),
]
