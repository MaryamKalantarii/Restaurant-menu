from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from accounts.models import Profile
from dashboard.admin.api.V1.serializers import AllProfileCustomerSerializer
from dashboard.admin.api.V1.paginations import UserListPagination
from dashboard.admin.api.V1.serializers import CreateCategorySerializer, CreateMenuItemSerializer, \
                UpdateCategorySerializer, UpdateMenuSerializer
from menu.models import MenuItem, Category
from reservations.models import Reservation
from reservations.api.V1.serializers import ReservationSerializer


class AllProfileCustomerAPIView(generics.ListAPIView):

    """List all user profiles (admin access only), with search, ordering, and pagination."""
    
    queryset = Profile.objects.select_related("user")
    serializer_class = AllProfileCustomerSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = UserListPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'phone_number', 'user__email']


class CreateMenuItemAPIView(generics.CreateAPIView):

    """Create a new menu item (admin only)."""

    queryset = MenuItem.objects.select_related("user").prefetch_related("category")
    serializer_class = CreateMenuItemSerializer
    permission_classes = [permissions.IsAdminUser]



class UpdateMenuAPIView(generics.UpdateAPIView):

    """Update a menu item (admin only)."""

    queryset = MenuItem.objects.select_related("user").prefetch_related("category")
    serializer_class = UpdateMenuSerializer
    permission_classes = [permissions.IsAdminUser]


class RemoveMenuAPIView(generics.DestroyAPIView):

    """Delete a menu item (admin only)."""

    queryset = MenuItem.objects.select_related("user").prefetch_related("category")
    serializer_class = UpdateMenuSerializer
    permission_classes = [permissions.IsAdminUser]


class CreateCategoryMenuAPIView(generics.CreateAPIView):

    """Create a new category (admin only)."""

    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer
    permission_classes = [permissions.IsAdminUser]



class UpdateCategoryMenuAPIView(generics.UpdateAPIView):

    """Update a category (admin only)."""

    queryset = Category.objects.all()
    serializer_class = UpdateCategorySerializer
    permission_classes = [permissions.IsAdminUser]


class RemoveCategoryMenuAPIView(generics.DestroyAPIView):

    """Delete a category (admin only)."""
    
    queryset = Category.objects.all()
    serializer_class = UpdateCategorySerializer
    permission_classes = [permissions.IsAdminUser]



class AdminReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.select_related("user")
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAdminUser]


class DeleteResevationAPIView(generics.DestroyAPIView):
    queryset = Reservation.objects.select_related("user")
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ReservationSerializer
