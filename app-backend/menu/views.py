from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import CategorySerializer, GetMenuItemSerializer
from .models import MenuItem, Category
from .paginations import MenuItemPagination




class MenuViewSet(ModelViewSet):

    """List all menu items with pagination, filtering, search, and ordering."""

    queryset = MenuItem.objects.select_related("user").prefetch_related("category")
    serializer_class = GetMenuItemSerializer
    pagination_class = MenuItemPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['description', 'category__title']
    ordering_fields = ['created_date', 'price']
    ordering = ['-created_date']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]


class CategoryViewSet(ModelViewSet):

    """List all categories with search and ordering."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
    ordering = ['title']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]