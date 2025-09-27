import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from reservations.models import Reservation
from datetime import date, time

User = get_user_model()

# ====== مسیرهای واقعی ======
PROFILE_URL = reverse('my-profile')
RESERVATION_URL = reverse('List-reserved')

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def customer_user(db):
    user = User.objects.create_user(
        email="customer@example.com",
        password="pass1234"
    )
    # اضافه کردن profile فرضی
    user.profile.phone_number = "09123456789"
    user.profile.save()
    return user

@pytest.fixture
def another_user(db):
    user = User.objects.create_user(
        email="other@example.com",
        password="pass1234"
    )
    user.profile.phone_number = "09987654321"
    user.profile.save()
    return user

@pytest.fixture
def customer_reservations(db, customer_user):
    # ساخت دو رزرو برای کاربر
    Reservation.objects.create(user=customer_user, date=date.today(), time=time(14,0), people=2)
    Reservation.objects.create(user=customer_user, date=date.today(), time=time(18,0), people=4)
    return Reservation.objects.filter(user=customer_user)

@pytest.fixture
def other_reservation(db, another_user):
    # رزرو برای کاربر دیگر
    return Reservation.objects.create(user=another_user, date=date.today(), time=time(16,0), people=3)

# ====== توابع کمکی ======
def auth_client(client: APIClient, user: User):
    client.force_authenticate(user=user)
    return client

# ====== تست‌ها ======

@pytest.mark.django_db
def test_profile_requires_auth(api_client):
    resp = api_client.get(PROFILE_URL)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_reservation_requires_auth(api_client):
    resp = api_client.get(RESERVATION_URL)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_get_profile(api_client, customer_user):
    client = auth_client(api_client, customer_user)
    resp = client.get(PROFILE_URL)
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    # فقط فیلدهای موجود در خروجی رو بررسی کن
    assert data.get("phone_number") == "09123456789"
    assert "first_name" in data
    assert "last_name" in data
    assert "image" in data


@pytest.mark.django_db
def test_get_reservations(api_client, customer_user, customer_reservations, other_reservation):
    client = auth_client(api_client, customer_user)
    resp = client.get(RESERVATION_URL)
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    # فقط رزروهای خودش را می‌بیند
    assert all(r["email"] == customer_user.email for r in data)
    assert len(data) == customer_reservations.count()
    # مطمئن می‌شویم رزرو کاربر دیگر نمایش داده نشده
    assert all(r["email"] != "other@example.com" for r in data)

@pytest.mark.django_db
def test_invalid_method_on_profile(api_client, customer_user):
    client = auth_client(api_client, customer_user)
    resp = client.post(PROFILE_URL, data={"foo": "bar"})
    assert resp.status_code in (status.HTTP_405_METHOD_NOT_ALLOWED, status.HTTP_403_FORBIDDEN)

@pytest.mark.django_db
def test_invalid_method_on_reservations(api_client, customer_user):
    client = auth_client(api_client, customer_user)
    resp = client.post(RESERVATION_URL, data={"foo": "bar"})
    assert resp.status_code in (status.HTTP_405_METHOD_NOT_ALLOWED, status.HTTP_403_FORBIDDEN)
