from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from reservations.models import Reservation
from rest_framework import permissions
from reservations.models import Reservation
from .serializers import AdminReservationSerializer,AdminUserSerializer
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from menu.models import MenuItem, Category, ProductStatusType
from menu.api.V1.serializers import MenuItemSerializer,CategorySerializer


User = get_user_model()


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class AdminReservationCreateView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = AdminReservationSerializer
    permission_classes = [IsAdminUser]



class AdminUserViewSet(ModelViewSet):
    queryset = User.objects.all().select_related('profile')
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]



class AdminMenuItemView(ModelViewSet):

    queryset = MenuItem.objects.filter(status=ProductStatusType.publish.value) 
    serializer_class = MenuItemSerializer 
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['description', 'category__title']
    ordering_fields = ['created_date', 'price']
    ordering = ['-created_date']
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class AdminCategoryView(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
    ordering = ['title']
