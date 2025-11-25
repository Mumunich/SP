import requests
import pytest
from faker import Faker

# ===== CONFIG =====
BASE_URL = "https://ru.yougile.com/api-v2/"
COMPANY_DATA = {
    "login": "rostOFfun@mail.ru",
    "password": "12051961r",
    "name": "Поток_66.0",
}
COMMON_HEADERS = {"Content-Type": "application/json"}

fake = Faker()


def get_company_id():
    response = requests.post(
        BASE_URL + "auth/companies", headers=COMMON_HEADERS, json=COMPANY_DATA
    )
    return response.json()["content"][0]["id"]


def get_api_key(company_id):
    auth_data = {
        "login": COMPANY_DATA["login"],
        "password": COMPANY_DATA["password"],
        "companyId": company_id,
    }
    response = requests.post(
        BASE_URL + "auth/keys", headers=COMMON_HEADERS, json=auth_data
    )
    return response.json()["key"]


def delete_api_key(api_key):
    response = requests.delete(
        BASE_URL + "auth/keys/" + api_key, headers=COMMON_HEADERS
    )
    return response.status_code


def get_user_id(api_key):
    headers = {**COMMON_HEADERS, "Authorization": f"Bearer {api_key}"}
    response = requests.get(BASE_URL + "users", headers=headers)
    return response.json()["content"][0]["id"]


def generate_fake_title():
    return fake.catch_phrase()


@pytest.fixture(scope="session")
def test_setup():
    """Всё что нужно для тестов"""
    company_id = get_company_id()
    api_key = get_api_key(company_id)
    user_id = get_user_id(api_key)
    headers = {**COMMON_HEADERS, "Authorization": f"Bearer {api_key}"}
    project_id = ""

    yield {
        "api_key": api_key,  # удалить
        "user_id": user_id,
        "company_id": company_id,  # удалить
        "headers": headers,
        "project_id": project_id,
    }

    delete_api_key(api_key)


# Положительные тесты
def test_create_project(test_setup):
    """Тест создания проекта"""
    data = {
        "title": generate_fake_title(),
        "users": {test_setup["user_id"]: "admin"},
    }
    response = requests.post(
        BASE_URL + "projects", headers=test_setup["headers"], json=data
    )
    test_setup["project_id"] = response.json()["id"]
    assert response.status_code == 201


def test_change_project(test_setup):
    """Тест редактирования проекта"""
    data = {"title": "Новое название, изменено тестом"}
    response = requests.put(
        BASE_URL + "projects/" + test_setup["project_id"],
        headers=test_setup["headers"],
        json=data,
    )
    assert response.status_code == 200


def test_getting_project_by_id(test_setup):
    """Тест получения проекта по id"""
    response = requests.get(
        BASE_URL + "projects/" + test_setup["project_id"],
        headers=test_setup["headers"],
    )
    assert response.status_code == 200


# Отрицательные тесты
def test_create_project_with_empty_tittle(test_setup):
    """Тест создания проекта без названия"""
    data = {"title": "", "users": {test_setup["user_id"]: "admin"}}
    response = requests.post(
        BASE_URL + "projects", headers=test_setup["headers"], json=data
    )
    assert response.status_code == 400


def test_change_project_with_invalid_parameter(test_setup):
    """Тест редактирования проекта с невалидным ID"""
    data = {
        "deleted": "ГосУслуги",
    }
    response = requests.put(
        BASE_URL + "projects/" + test_setup["project_id"] + "123asd",
        headers=test_setup["headers"],
        json=data,
    )
    assert response.status_code == 400


def test_getting_project_by_invalid_id(test_setup):
    """Тест получения проекта по невалидному ID"""
    response = requests.get(
        BASE_URL + "projects/" + test_setup["project_id"] + "123asd",
        headers=test_setup["headers"],
    )
    assert response.status_code == 404
