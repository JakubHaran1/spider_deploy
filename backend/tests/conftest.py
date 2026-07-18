import pytest

from spider_app.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def user():
    user = User.objects.create_user(
        username="admin_test", email="admin_test@wp.pl", password="admin_test")

    return user


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def auth_client(api_client, user):
    token = RefreshToken.for_user(user)
    access = str(token.access_token)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
    return api_client
