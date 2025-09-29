import pytest
from rest_framework.test import APIClient
from rest_framework import status
from menu.models import MenuItem, Category, ProductStatusType
from accounts.models import CustomeUser

MENU_ITEMS_URL = "/menu/api/V1/menu-items/"
CATEGORIES_URL = "/menu/api/V1/categories/"

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def customer_user(db):
    return CustomeUser.objects.create_user(email="customer@example.com", password="pass1234")

@pytest.fixture
def categories(db):
    cat1 = Category.objects.create(title="دسر")
    cat2 = Category.objects.create(title="نوشیدنی")
    return [cat1, cat2]

@pytest.fixture
def menu_items(db, customer_user, categories):
    # فقط آیتم‌های publish برای تست
    item1 = MenuItem.objects.create(
        user=customer_user,
        title="کیک شکلاتی",
        description="خوشمزه",
        price=100000,
        discount_percent=10,
        status=ProductStatusType.publish.value,
        stock=5,
    )
    item1.category.set([categories[0]])

    item2 = MenuItem.objects.create(
        user=customer_user,
        title="چای سبز",
        description="آرامش‌بخش",
        price=20000,
        discount_percent=0,
        status=ProductStatusType.publish.value,
        stock=0,
    )
    item2.category.set([categories[1]])

    item3 = MenuItem.objects.create(
        user=customer_user,
        title="قهوه",
        description="صبحگاهی",
        price=50000,
        discount_percent=5,
        status=ProductStatusType.draft.value,  # draft، نباید در خروجی باشد
        stock=10,
    )
    item3.category.set([categories[1]])

    return [item1, item2, item3]

@pytest.mark.django_db
def test_get_menu_items_list(api_client, menu_items):
    resp = api_client.get(MENU_ITEMS_URL)
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    # فقط آیتم‌های publish برگردند
    assert len(data) == 2
    titles = [item['title'] for item in data]
    assert "کیک شکلاتی" in titles
    assert "چای سبز" in titles
    for item in data:
        assert 'detail_link' in item

@pytest.mark.django_db
def test_get_categories_list(api_client, categories):
    resp = api_client.get(CATEGORIES_URL)
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    titles = [c['title'] for c in data]
    assert "دسر" in titles
    assert "نوشیدنی" in titles

@pytest.mark.django_db
def test_invalid_method_on_menu_items(api_client):
    resp = api_client.post(MENU_ITEMS_URL, data={"title":"foo"})
    assert resp.status_code in (status.HTTP_405_METHOD_NOT_ALLOWED, status.HTTP_403_FORBIDDEN)

@pytest.mark.django_db
def test_invalid_method_on_categories(api_client):
    resp = api_client.post(CATEGORIES_URL, data={"title":"foo"})
    assert resp.status_code in (status.HTTP_405_METHOD_NOT_ALLOWED, status.HTTP_403_FORBIDDEN)
