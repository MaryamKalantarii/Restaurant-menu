import pytest
from rest_framework import status
from rest_framework.test import APIClient
from accounts.models import CustomeUser


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_successful_registration(client, mocker):
    url = "/accounts/api/V1/registration/"

    data = {
        "email": "testuser@example.com",
        "password": "strong_password_123",
        "password_confirm": "strong_password_123",
    }

    # جلوگیری از اجرای واقعی celery
    mocked_task = mocker.patch("accounts.api.V1.tasks.send_email_with_celery.delay")

    response = client.post(url, data, format="json")

    # بررسی موفقیت
    assert response.status_code == status.HTTP_200_OK
    assert "ایمیل ارسال شد" in response.data["detail"]

    # بررسی ساخت کاربر
    user = CustomeUser.objects.get(email=data["email"])
    assert user is not None

    # بررسی اینکه celery task صدا زده شد
    mocked_task.assert_called_once()


@pytest.mark.django_db
def test_passwords_do_not_match(client):
    url = "/accounts/api/V1/registration/"

    data = {
        "email": "failuser@example.com",
        "password": "password123",
        "password_confirm": "wrongpassword",
    }

    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    # سرور ممکنه خطا رو در کلیدهای مختلف بده، پس همه رو چک می‌کنیم
    assert (
        "password" in response.data
        or "password_confirm" in response.data
        or "non_field_errors" in response.data
        or "detail" in response.data
    )


@pytest.mark.django_db
def test_duplicate_email_registration(client, django_user_model):
    url = "/accounts/api/V1/registration/"

    # کاربر از قبل وجود دارد
    django_user_model.objects.create_user(
        email="duplicate@example.com", password="password123"
    )

    data = {
        "email": "duplicate@example.com",
        "password": "password123",
        "password_confirm": "password123",
    }

    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email" in response.data
