from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Profile
from menu.models import MenuItem, Category, GalleryMenu


User = get_user_model()



class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class AllProfileCustomerSerializer(serializers.ModelSerializer):
    user = GetUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "first_name", "last_name", "phone_number", "image", "created_date", "updated_date"]


class CreateCategorySerializer(serializers.ModelSerializer):

    """Serialize category data for creation (only title)."""

    class Meta:
        model = Category
        fields = ['title']


class UpdateCategorySerializer(serializers.ModelSerializer):

    """Serialize category data for update (title and slug)."""

    class Meta:
        model = Category
        fields = ['title', 'slug']


class GalleryMenuSerializer(serializers.ModelSerializer):

    """Serialize image gallery related to a menu item."""

    class Meta:
        model = GalleryMenu
        fields = ['id', 'image']


class CreateMenuItemSerializer(serializers.ModelSerializer):

    """Serialize menu item data for creation including gallery images."""

    menu_item = GalleryMenuSerializer(many=True)

    class Meta:
        model = MenuItem
        fields = ["category", "title", "description", "image", "menu_item", "stock", "status", "price", "discount_percent",
                  "is_featured", "preparation_time",
                  ]
    
    def create(self, validated_data):
        gallery_data = validated_data.pop("menu_item", [])
        menu_items = MenuItem.objects.create(**validated_data)

        for image_data in gallery_data:
            GalleryMenu.objects.create(menu=menu_items, **image_data)

        return menu_items
    

class UpdateMenuSerializer(serializers.ModelSerializer):

    """Serialize all fields of menu item for update (admin use)."""

    class Meta:
        model = MenuItem
        fields = "__all__"

