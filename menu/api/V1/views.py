from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import MenuItemSerializer, CategorySerializer 
from menu.models import MenuItem, Category, ProductStatusType


class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.filter(status=ProductStatusType.publish.value) 
    serializer_class = MenuItemSerializer 
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['description', 'category__title']
    ordering_fields = ['created_date', 'price']
    ordering = ['-created_date']

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)


        
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 
    lookup_field = 'slug'

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
    ordering = ['title']

