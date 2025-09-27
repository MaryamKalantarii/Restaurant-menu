import pytest
from rest_framework import status
from rest_framework.test import APIClient
from accounts.models import CustomeUser
from rest_framework_simplejwt.tokens import RefreshToken


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





@pytest.mark.django_db
def test_is_verified_success(client):
    user = CustomeUser.objects.create_user(
        email="test@example.com", password="password123", is_verified=False
    )
    token = str(RefreshToken.for_user(user).access_token)
    
    url = f"/accounts/api/V1/is-verified/{token}/"
    response = client.get(url)
    
    user.refresh_from_db()
    assert user.is_verified is True
    assert response.status_code == 302
    assert "status=success" in response.url

@pytest.mark.django_db
def test_is_verified_invalid_token(client):
    url = "/accounts/api/V1/is-verified/invalidtoken/"
    response = client.get(url)
    assert response.status_code == 302
    assert "status=error" in response.url



@pytest.mark.django_db
def test_resend_email_success(client, mocker):
    user = CustomeUser.objects.create_user(
        email="testuser@example.com", password="password123", is_verified=False
    )
    mocked_task = mocker.patch("accounts.api.V1.tasks.send_email_with_celery.delay")

    url = "/accounts/api/V1/resend/"
    response = client.post(url, {"email": user.email}, format="json")

    assert response.status_code == 200
    assert "ارسال مجدد ایمیل" in response.data["detail"]
    mocked_task.assert_called_once()

@pytest.mark.django_db
def test_resend_email_already_verified(client, mocker):
    user = CustomeUser.objects.create_user(
        email="verified@example.com", password="password123", is_verified=True
    )
    mocked_task = mocker.patch("accounts.api.V1.tasks.send_email_with_celery.delay")

    url = "/accounts/api/V1/resend/"
    response = client.post(url, {"email": user.email}, format="json")

    assert response.status_code == 200
    assert "ایمیل شما قبلا تایید شده است" in response.data["detail"]
    mocked_task.assert_not_called()




@pytest.mark.django_db
def test_change_password_success(client):
    user = CustomeUser.objects.create_user(
        email="test@example.com", password="old_password123"
    )
    client.force_authenticate(user=user)

    url = "/accounts/api/V1/change-password/"
    data = {
        "old_password": "old_password123",
        "new_password1": "new_password456",
        "new_password2": "new_password456",
    }

    response = client.post(url, data, format="json")
    user.refresh_from_db()
    
    assert response.status_code == status.HTTP_200_OK
    assert "رمز عبور با موفقیت تغییر کرد" in response.data["detail"]
    assert user.check_password("new_password456") is True

@pytest.mark.django_db
def test_change_password_wrong_old(client):
    user = CustomeUser.objects.create_user(
        email="test@example.com", password="old_password123"
    )
    client.force_authenticate(user=user)

    url = "/accounts/api/V1/change-password/"
    data = {
        "old_password": "wrong_old_password",
        "new_password1": "new_password456",
        "new_password2": "new_password456",
    }

    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_change_password_mismatch(client):
    user = CustomeUser.objects.create_user(
        email="test@example.com", password="old_password123"
    )
    client.force_authenticate(user=user)

    url = "/accounts/api/V1/change-password/"
    data = {
        "old_password": "old_password123",
        "new_password1": "new_password456",
        "new_password2": "different_password",
    }

    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST






@pytest.mark.django_db
def test_password_reset_request_success(client, mocker):
    user = CustomeUser.objects.create_user(
        email="testuser@example.com", password="password123"
    )
    mocked_task = mocker.patch("accounts.api.V1.tasks.send_email_with_celery.delay")

    url = "/accounts/api/V1/reset-password/"
    response = client.post(url, {"email": user.email}, format="json")

    assert response.status_code == 200
    assert "لینک تغییر رمز عبور" in response.data["detail"]
    mocked_task.assert_called_once()

@pytest.mark.django_db
def test_password_reset_request_email_not_found(client, mocker):
    mocked_task = mocker.patch("accounts.api.V1.tasks.send_email_with_celery.delay")

    url = "/accounts/api/V1/reset-password/"
    response = client.post(url, {"email": "notfound@example.com"}, format="json")


    assert response.status_code == 400  
    mocked_task.assert_not_called()




@pytest.mark.django_db
def test_password_reset_confirm_success(client):
    user = CustomeUser.objects.create_user(
        email="test@example.com", password="old_password123"
    )
    token = str(RefreshToken.for_user(user).access_token)

    url = f"/accounts/api/V1/reset-password-confirm/{token}/"
    data = {"new_password1": "newpass456", "new_password2": "newpass456"}

    response = client.post(url, data, format="json")
    user.refresh_from_db()

    assert response.status_code == 200
    assert "رمز عبور با موفقیت بازنشانی شد" in response.data["detail"]
    assert user.check_password("newpass456") is True

@pytest.mark.django_db
def test_password_reset_confirm_invalid_token(client):
    url = "/accounts/api/V1/reset-password-confirm/invalidtoken/"
    data = {"new_password1": "newpass456", "new_password2": "newpass456"}

    response = client.post(url, data, format="json")
    assert response.status_code == 400
    assert "توکن نامعتبر یا منقضی شده است" in response.data["detail"]
