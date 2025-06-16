from .serializers import MenuItemSerializer, CategorySerializer 
from menu.models import MenuItem, Category, ProductStatusType
from rest_framework.generics import ListAPIView




class MenuItemView(ListAPIView):

    queryset = MenuItem.objects.filter(status=ProductStatusType.publish.value) 
    serializer_class = MenuItemSerializer 


class CategoryView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
  