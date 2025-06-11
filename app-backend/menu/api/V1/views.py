from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import CategorySerializer, GetMenuItemSerializer
from menu.models import MenuItem, Category
from ...api.V1.paginations import MenuItemPagination




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
