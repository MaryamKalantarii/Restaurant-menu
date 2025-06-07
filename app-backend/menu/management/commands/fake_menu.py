from django.core.management.base import BaseCommand
from faker import Faker
import random
from pathlib import Path
from django.core.files import File
from django.utils.text import slugify
from menu.models import MenuItem, Category
from accounts.models import CustomeUser

BASE_DIR = Path(__file__).resolve().parent

class Command(BaseCommand):
    help = 'Generate fake menu items with image and categories'

    def handle(self, *args, **options):
        fake = Faker('en_US')
      
        
        default_categories = [
            {"title": "صبحانه", "slug": "breakfast"},
            {"title": "ناهار", "slug": "lunch"},
            {"title": "شام", "slug": "dinner"},
            {"title": "پیش‌غذا", "slug": "starters"},
            {"title": "پیشنهاد سرآشپز", "slug": "special"},
        ]

        for cat in default_categories:
            obj, created = Category.objects.get_or_create(slug=cat["slug"], defaults={"title": cat["title"]})
            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ دسته‌بندی اضافه شد: {cat['title']}"))


        image_list = [f"images/menu-item-{i}.png" for i in range(1, 6)] 
        categories = list(Category.objects.all())
        user = CustomeUser.objects.first()

        if not categories:
            self.stdout.write(self.style.WARNING("❌ No categories found. Please create some first."))
            return

        if not user:
            self.stdout.write(self.style.WARNING("❌ No user found. Please create a superuser first."))
            return

        for _ in range(15): 
            title = fake.sentence(nb_words=2)
            slug = slugify(title, allow_unicode=True)
            description = fake.text(max_nb_chars=150)

            selected_image = random.choice(image_list)
            image_path = BASE_DIR / selected_image

            if not image_path.exists():
                self.stdout.write(self.style.WARNING(f"⚠️ Image not found: {selected_image}"))
                continue

            with open(image_path, "rb") as img_file:
                image_file = File(img_file, name=Path(selected_image).name)

                item = MenuItem.objects.create(
                    user=user,
                    title=title,
                    slug=slug,
                    description=description,
                    image1=image_file,
                    stock=random.randint(0, 20),
                    status=1,  # Published
                    price=random.randint(50000, 200000),
                    discount_percent=random.choice([0, 10, 20]),
                    views=random.randint(0, 200),
                    is_featured=random.choice([True, False]),
                    preparation_time=random.randint(5, 45),
                )

                item.category.set(random.sample(categories, k=random.randint(1, 2)))

        self.stdout.write(self.style.SUCCESS("✅ Fake menu items created successfully."))
