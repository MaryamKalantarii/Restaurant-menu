import pytest
from django.utils import timezone
from rest_framework.test import APIClient
from accounts.models import CustomeUser
from reservations.models import Reservation
from datetime import timedelta, time
from unittest.mock import patch
@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def create_user_with_profile(db):
    def make_user(email="user@example.com", phone="09120000000"):
        user = CustomeUser.objects.create_user(email=email, password="testpass123")
        # پروفایل به خاطر سیگنال ساخته میشه → فقط آپدیتش می‌کنیم
        user.profile.first_name = "Test"
        user.profile.last_name = "User"
        user.profile.phone_number = phone
        user.profile.save()
        return user
    return make_user


@pytest.mark.django_db
def test_successful_reservation(client, create_user_with_profile):
    user = create_user_with_profile()
    client.force_authenticate(user=user)

    data = {
        "date": (timezone.now().date() + timedelta(days=1)).isoformat(),
        "time": "13:00:00",
        "people": 2,
    }

    response = client.post("/reservations/api/V1/reserve/", data, format="json")
    assert response.status_code == 201
    assert Reservation.objects.count() == 1
    assert Reservation.objects.first().user == user


@pytest.mark.django_db
def test_reservation_fails_without_profile(client, db):
    user = CustomeUser.objects.create_user(email="noprof@example.com", password="testpass123")
    client.force_authenticate(user=user)

    data = {
        "date": (timezone.now().date() + timedelta(days=1)).isoformat(),
        "time": "14:00:00",
        "people": 3,
    }

    response = client.post("/reservations/api/V1/reserve/", data, format="json")
    assert response.status_code == 400
    # اینجا response.data لیست هست
    assert any("پروفایل شما کامل نیست" in str(err) or "شماره تلفن" in str(err) for err in response.data)


@pytest.mark.django_db
def test_reservation_fails_with_empty_phone(client, create_user_with_profile):
    user = create_user_with_profile(phone="")  # شماره خالی
    client.force_authenticate(user=user)

    data = {
        "date": (timezone.now().date() + timedelta(days=1)).isoformat(),
        "time": "15:00:00",
        "people": 2,
    }

    response = client.post("/reservations/api/V1/reserve/", data, format="json")
    assert response.status_code == 400
    # اینجا هم لیست میشه
    assert any("شماره تلفن" in str(err) for err in response.data)



@pytest.mark.django_db
def test_reservation_fails_with_past_date(client, create_user_with_profile):
    user = create_user_with_profile()
    client.force_authenticate(user=user)

    data = {
        "date": (timezone.now().date() - timedelta(days=1)).isoformat(),
        "time": "16:00:00",
        "people": 2,
    }

    response = client.post("/reservations/api/V1/reserve/", data, format="json")
    assert response.status_code == 400
    # اینجا میاد داخل non_field_errors
    assert "non_field_errors" in response.data
    assert any("تاریخ رزرو نمی‌تواند در گذشته باشد" in str(err) for err in response.data["non_field_errors"])


@pytest.mark.django_db
def test_reservation_fails_with_invalid_time(client, create_user_with_profile):
    user = create_user_with_profile()
    client.force_authenticate(user=user)

    data = {
        "date": (timezone.now().date() + timedelta(days=1)).isoformat(),
        "time": "23:30:00",  # خارج از بازه 12 تا 22
        "people": 2,
    }

    response = client.post("/reservations/api/V1/reserve/", data, format="json")
    assert response.status_code == 400
    assert "رزرو فقط بین ساعت 12 تا 22 ممکن است" in str(response.data)





@pytest.mark.django_db
@patch("reservations.api.V1.tasks.send_reservation_email.delay")  # مسیر درست ویو رو بزن
def test_reservation_triggers_email(mock_send_email, client, create_user_with_profile):
    user = create_user_with_profile(phone="09120000000")
    client.force_authenticate(user=user)

    data = {
        "date": (timezone.now().date() + timedelta(days=1)).isoformat(),
        "time": "14:00:00",
        "people": 2,
    }

    response = client.post("/reservations/api/V1/reserve/", data, format="json")

    assert response.status_code == 201  # رزرو موفق
    # ✅ چک می‌کنیم که ایمیل صدا زده شده
    mock_send_email.assert_called_once()
    args, kwargs = mock_send_email.call_args
    assert user.email in args  # ایمیل کاربر داخل آرگومان‌هاست





@pytest.mark.django_db
def test_my_reservations_returns_only_user_reservations(client, create_user_with_profile):
    user1 = create_user_with_profile(phone="09120000000")
    user2 = create_user_with_profile(email="other@example.com", phone="09350000000")
    client.force_authenticate(user=user1)

    # رزروهای کاربر ۱
    Reservation.objects.create(user=user1, date=timezone.now().date() + timedelta(days=1), time="13:00", people=2)
    Reservation.objects.create(user=user1, date=timezone.now().date() + timedelta(days=2), time="14:00", people=3)

    # رزرو کاربر ۲
    Reservation.objects.create(user=user2, date=timezone.now().date() + timedelta(days=1), time="15:00", people=4)

    response = client.get("/reservations/api/V1/user-reservations/")

    assert response.status_code == 200
    assert len(response.data) == 2  # فقط رزروهای user1
    for res in response.data:
        assert res["email"] == user1.email


@pytest.mark.django_db
def test_my_reservations_requires_authentication(client):
    response = client.get("/reservations/api/V1/user-reservations/")
    assert response.status_code == 401