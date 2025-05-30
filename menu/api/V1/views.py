from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import MenuItemSerializer, CategorySerializer 
from .permissions import IsAdminAndVerifiedOrReadOnly
from .models import MenuItem, Category, ProductStatusType

class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.filter(status=ProductStatusType.publish.value) 
    serializer_class = MenuItemSerializer 
    permission_classes = [IsAdminAndVerifiedOrReadOnly]
    lookup_field = 'slug'

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['description', 'category__title']
    ordering_fields = ['created_date', 'price']
    ordering = ['-created_date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminAndVerifiedOrReadOnly]
    lookup_field = 'slug'

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
    ordering = ['title']
