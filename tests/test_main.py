from pathlib import Path

import pytest
from rest_framework import status

from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_register_user(api_client):
    payload = dict(username="admin3",
                   email="admin3@wp.pl",
                   password="admin3")
    response = api_client.post("/api/users/", payload)
    data = response.data
    assert payload["username"] == data["username"]
    assert payload["password"] not in data


@pytest.mark.django_db
def test_login_user(api_client):
    payload = dict(username="admin3",
                   email="admin3@wp.pl",
                   password="admin3")
    api_client.post("/api/users/", payload)

    response = api_client.post(
        "/api/users/login/", dict(username=payload["username"], password=payload["password"]))

    data = response.status_code
    assert data == status.HTTP_200_OK


@pytest.mark.django_db
def test_login_user_fail(api_client):
    response = api_client.post(
        "/api/users/login/", dict(username="username", password="password"))

    data = response.status_code
    assert data == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_create_spider(auth_client):
    img_path = Path(__file__).parent / "test_img.webp"

    with open(img_path, "rb") as img:
        uploaded_file = SimpleUploadedFile(
            name="./test_img.webp", content=img.read(), content_type="image/webp")

    payload = dict(name="spider_test", type="spider_test",
                   description="spider_test", tags="spider_test", spider_img=uploaded_file)

    response = auth_client.post(
        "/api/spiders/", payload, format="multipart")

    data = response.status_code
    assert data == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_spider_without_auth(client):
    img_path = Path(__file__).parent / "test_img.webp"

    with open(img_path, "rb") as img:
        uploaded_file = SimpleUploadedFile(
            name="./test_img.webp", content=img.read(), content_type="image/webp")

    payload = dict(name="spider_test", type="spider_test",
                   description="spider_test", tags="spider_test", spider_img=uploaded_file)

    response = client.post(
        "/api/spiders/", payload, format="multipart")

    data = response.status_code
    assert data == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_spider(auth_client):
    img_path = Path(__file__).parent / "test_img.webp"

    with open(img_path, "rb") as img:
        uploaded_file = SimpleUploadedFile(
            name="./test_img.webp", content=img.read(), content_type="image/webp")

    payload = dict(name="spider_test", type="spider_test",
                   description="spider_test", tags="spider_test", spider_img=uploaded_file)

    create_response = auth_client.post(
        "/api/spiders/", payload, format="multipart")

    data_create = create_response.data

    get_response = auth_client.get(
        f"/api/spiders/{data_create["id"]}/")

    response_data = get_response.data

    get_data = response_data
    assert get_data["name"] == payload["name"]


@pytest.mark.django_db
def test_put_spider(auth_client):
    img_path = Path(__file__).parent / "test_img.webp"

    with open(img_path, "rb") as img:
        uploaded_file = SimpleUploadedFile(
            name="./test_img.webp", content=img.read(), content_type="image/webp")

    payload = dict(name="spider_test", type="spider_test",
                   description="spider_test", tags="spider_test", spider_img=uploaded_file)

    create_response = auth_client.post(
        "/api/spiders/", payload, format="multipart")

    data_create = create_response.data

    with open(img_path, "rb") as img:
        uploaded_file2 = SimpleUploadedFile(
            name="./test_img.webp", content=img.read(), content_type="image/webp")

    payload2 = dict(name="spider_test2", type="spider_test2",
                    description="spider_test2", tags="spider_test2", spider_img=uploaded_file2)

    get_response = auth_client.patch(
        f"/api/spiders/{data_create['id']}/", payload2, format="multipart")

    print("d", get_response.data)
    response_data = get_response.data

    assert response_data["name"] == payload2["name"]
