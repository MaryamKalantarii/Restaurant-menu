from rest_framework import serializers
from ...models import MenuItem, Category, GalleryMenu



class CategorySerializer(serializers.ModelSerializer):

    """Serialize category data for listing and detail views."""

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


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


class GetMenuItemSerializer(serializers.ModelSerializer):

    """Serialize menu item for listing and detail, with extra computed fields."""
    
    category = CategorySerializer(many=True, read_only=True)
    detail_link = serializers.SerializerMethodField()
    get_price = serializers.SerializerMethodField()
    is_discounted = serializers.BooleanField(read_only=True)
    is_published = serializers.BooleanField(read_only=True)
    is_out_of_stock = serializers.BooleanField(read_only=True)
    menu_item = GalleryMenuSerializer(many=True)

    class Meta:
        model = MenuItem
        fields = [
            'id',
            'user',
            'category',
            'title',
            'slug',
            'description',
            'image',
            'menu_item',
            'stock',
            'status',
            'price',
            'get_price',
            'discount_percent',
            'views',
            'is_featured',
            'preparation_time',
            'created_date',
            'updated_date',
            'is_discounted',
            'is_published',
            'is_out_of_stock',
            'detail_link',
        ]
        read_only_fields = ['created_date', 'updated_date', 'views']

    def get_detail_link(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'/api/v1/menu/{obj.slug}/')  

    def get_get_price(self, obj):
        return obj.get_price()  
