from rest_framework import serializers
from ...models import MenuItem, Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serialize category data for listing and detail views.
    """

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']



class MenuItemSerializer(serializers.ModelSerializer):
    # فقط برای گرفتن اطلاعات
    category = CategorySerializer(many=True, read_only=True)

    # فقط برای ساختن یا آپدیت (در post/put)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True
    )

    detail_link = serializers.SerializerMethodField()
    get_price = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = [
            'id',
            'user',
            'category',       # فقط خواندنی
            'category_ids',   # فقط نوشتنی
            'title',
            'slug',
            'description',
            'image',
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
        read_only_fields = [
            'created_date', 'updated_date', 'views',
            'get_price', 'detail_link',
            'is_discounted', 'is_published', 'is_out_of_stock'
        ]

    def create(self, validated_data):
        categories = validated_data.pop('category_ids', [])
        item = MenuItem.objects.create(**validated_data)
        item.category.set(categories)
        return item

    def update(self, instance, validated_data):
        categories = validated_data.pop('category_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if categories is not None:
            instance.category.set(categories)
        return instance

    def get_detail_link(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'/api/V1/menu/{obj.slug}/')

    def get_get_price(self, obj):
        return obj.get_price()
