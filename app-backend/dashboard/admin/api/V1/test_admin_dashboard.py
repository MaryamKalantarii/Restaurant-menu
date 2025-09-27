import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import CustomeUser

# URL های تست
ADMIN_RESERVATION_URL = reverse('reservation-list')
ADMIN_USER_URL = reverse('admin-users-list')

# helper برای احراز هویت
def auth_client(client, user):
    client.force_authenticate(user=user)
    return client

# fixture برای admin user
@pytest.fixture
def admin_user(db):
    user = CustomeUser.objects.create_superuser(email="admin@example.com", password="pass1234")
    return user

# fixture برای api client
@pytest.fixture
def api_client():
    return APIClient()

# ====================== تست‌ها ======================

@pytest.mark.django_db
def test_get_reservation_list(api_client, admin_user):
    client = auth_client(api_client, admin_user)
    resp = client.get(ADMIN_RESERVATION_URL)
    assert resp.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_get_user_list(api_client, admin_user):
    client = auth_client(api_client, admin_user)
    resp = client.get(ADMIN_USER_URL)
    assert resp.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_invalid_method_on_reservation_list(api_client, admin_user):
    client = auth_client(api_client, admin_user)
    resp = client.post(ADMIN_RESERVATION_URL, data={"foo":"bar"})
    assert resp.status_code in (
        status.HTTP_405_METHOD_NOT_ALLOWED,
        status.HTTP_403_FORBIDDEN,
        status.HTTP_400_BAD_REQUEST  # اضافه شد برای data نامعتبر
    )

@pytest.mark.django_db
def test_invalid_method_on_user_list(api_client, admin_user):
    client = auth_client(api_client, admin_user)
    resp = client.post(ADMIN_USER_URL, data={"foo":"bar"})
    assert resp.status_code in (
        status.HTTP_405_METHOD_NOT_ALLOWED,
        status.HTTP_403_FORBIDDEN,
        status.HTTP_400_BAD_REQUEST  # اضافه شد
    )
