import requests
BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_1_returns_200_and_expected_fields():
    r = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert r.status_code == 200

    data = r.json()
    # Проверяем наличие ключей
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

    # Проверяем конкретное значение id
    assert data["id"] == 1


def test_get_users_returns_list_and_non_empty():
    r = requests.get(f"{BASE_URL}/users", timeout=10)
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0

    # Проверим структуру первого пользователя
    first = data[0]
    assert "id" in first
    assert "name" in first
    assert "email" in first


def test_get_nonexistent_post_returns_404_or_empty_object():
    """
    У JSONPlaceholder часто для несуществующих ресурсов:
    - статус 404
    или
    - 200 + пустой объект {}
    (в разных окружениях бывает по-разному)
    """
    r = requests.get(f"{BASE_URL}/posts/0", timeout=10)

    if r.status_code == 404:
        assert True
    else:
        # если 200 — ожидаем пустой объект
        assert r.status_code == 200
        assert r.json() == {}
