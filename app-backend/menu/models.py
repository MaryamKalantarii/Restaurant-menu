from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(allow_unicode=True, unique=True, verbose_name="نامک")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"


class ProductStatusType(models.IntegerChoices):
    publish = 1, "نمایش"
    draft = 2, "عدم نمایش"


class MenuItem(models.Model):
    user = models.ForeignKey('accounts.CustomeUser', on_delete=models.CASCADE, related_name='menu_items', null=True, blank=True, verbose_name="کاربر")
    category = models.ManyToManyField(Category, verbose_name="دسته‌بندی‌ها")
    title = models.CharField(max_length=255, verbose_name="نام آیتم")
    slug = models.SlugField(allow_unicode=True, unique=True, verbose_name="نامک")
    description = models.TextField(verbose_name="توضیحات")
    image1 = models.ImageField(upload_to='menu_items', verbose_name="تصویر اصلی")
    image2 = models.ImageField(upload_to='menu_items', null=True, blank=True, verbose_name="تصویر دوم")

    stock = models.PositiveIntegerField(default=0, verbose_name="موجودی")
    status = models.IntegerField(choices=ProductStatusType.choices, default=ProductStatusType.publish.value, verbose_name="وضعیت")
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0, verbose_name="قیمت")
    discount_percent = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="درصد تخفیف")
    views = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")

    is_featured = models.BooleanField(default=False, verbose_name="آیتم ویژه")
    preparation_time = models.PositiveIntegerField(default=15, verbose_name="مدت زمان آماده‌سازی (دقیقه)")  # اینجا اضافه شد

    created_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    class Meta:
        ordering = ["-created_date"]
        verbose_name = "آیتم منو"
        verbose_name_plural = "آیتم‌های منو"

    def __str__(self):
        return self.title

    def get_price(self):
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        return round(self.price - discount_amount)

    def is_discounted(self):
        return self.discount_percent != 0

    def is_published(self):
        return self.status == ProductStatusType.publish.value

    @property
    def is_out_of_stock(self):
        return self.stock == 0
