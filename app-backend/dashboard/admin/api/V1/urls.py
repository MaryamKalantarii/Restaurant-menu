from django.urls import path
from dashboard.admin.api.V1.views import *


urlpatterns = [
    path("all_profile/", AllProfileCustomerAPIView.as_view(), name="all_profile"),
    path("create_menu/", CreateMenuItemAPIView.as_view(), name="create_menu"),
    path("update_menu/<int:pk>/", UpdateMenuAPIView.as_view(), name="update_menu"),
    path("remove_menu/<int:pk>/", RemoveMenuAPIView.as_view(), name="remove_menu"),
    path("create_category/", CreateCategoryMenuAPIView.as_view(), name="create_category_menu"),
    path("update_category/<int:pk>/", UpdateCategoryMenuAPIView.as_view(), name="update_category"),
    path("remove_category/<int:pk>/", RemoveCategoryMenuAPIView.as_view(), name="remove_category"),
    path('reserve-list_admin/', AdminReservationListView.as_view(), name='reserve-list-admin'),
    path('delete-reserve/<int:pk>/', DeleteResevationAPIView.as_view(), name='delete-reserve'),
]
