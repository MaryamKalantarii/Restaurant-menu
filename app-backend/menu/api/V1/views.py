from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import CategorySerializer, CreateMenuItemSerializer, GetMenuItemSerializer,\
                             UpdateMenuSerializer, CreateCategorySerializer, UpdateCategorySerializer
from menu.models import MenuItem, Category
from ...api.V1.paginations import MenuItemPagination



class CreateMenuItemAPIView(generics.CreateAPIView):

    """Create a new menu item (admin only)."""

    queryset = MenuItem.objects.select_related("user").prefetch_related("category")
    serializer_class = CreateMenuItemSerializer
    permission_classes = [permissions.IsAdminUser]


class GetListItemMenuAPIView(generics.ListAPIView):

    """List all menu items with pagination, filtering, search, and ordering."""

    queryset = MenuItem.objects.select_related("user").prefetch_related("category")
    serializer_class = GetMenuItemSerializer
    pagination_class = MenuItemPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['description', 'category__title']
    ordering_fields = ['created_date', 'price']
    ordering = ['-created_date']


class GetItemMenuAPIView(generics.RetrieveAPIView):

    """Retrieve a single menu item by slug."""

    queryset = MenuItem.objects.select_related("user").prefetch_related("category")
    serializer_class = GetMenuItemSerializer
    lookup_field = "slug"



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


class GetListCategoryMenuAPIView(generics.ListAPIView):

    """List all categories with search and ordering."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
    ordering = ['title']


class GetCategoryMenuAPIView(generics.RetrieveAPIView):

    """Retrieve a single category by slug."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"


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
