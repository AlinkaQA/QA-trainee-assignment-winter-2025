import requests
import config

# 1. Успешное создание объявления
def test_create_item():
    body = {
        "sellerID": 112277,
        "name": "Example Item",
        "price": 1000,
        "description": "Description of the item"
    }
    response = requests.post(f"{config.BASE_URL}/item", json=body)

    assert response.status_code == 200
    assert "status" in response.json()

# 2. Создание объявления без sellerID (Негативный тест)
def test_create_item_without_sellerID():
    body = {
        "name": "Example Item",
        "price": 1000,
        "description": "Description of the item"
    }
    response = requests.post(f"{config.BASE_URL}/item", json=body)

    assert response.status_code == 400
    assert response.json()["message"] == "sellerID is required"

# 3. Получение существующего объявления
def test_get_existing_item():
    item_id = "271a2549-611b-4ca4-abf3-eb0bc8838836"  # Заменить на существующий itemID
    response = requests.get(f"{config.BASE_URL}/item/{item_id}")

    assert response.status_code == 200
    assert "name" in response.json()[0]
    assert "price" in response.json()[0]

# 4. Получение несуществующего объявления
def test_get_non_existing_item():
    item_id = "cdba6dea-d852-432a-b46e-ad1a2ac20ac9"  # Заменить на несуществующий itemID
    response = requests.get(f"{config.BASE_URL}/item/{item_id}")

    assert response.status_code == 404
    assert response.json()["result"]["message"] == f"item {item_id} not found"

# 5. Получение всех объявлений существующего продавца
def test_get_items_by_seller():
    seller_id = 112277  # Заменить на существующий sellerID
    response = requests.get(f"{config.BASE_URL}/{seller_id}/item")

    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ожидаем список

# 6. Получение объявлений для sellerID, у которого нет объявлений
def test_get_items_for_seller_with_no_items():
    seller_id = 116677  # Заменить на sellerID без объявлений
    response = requests.get(f"{config.BASE_URL}/{seller_id}/item")

    assert response.status_code == 200
    assert response.json() == []  # Пустой список

# 7. Получение статистики существующего объявления
def test_get_statistic_for_existing_item():
    item_id = "271a2549-611b-4ca4-abf3-eb0bc8838836"  # Заменить на существующий itemID
    response = requests.get(f"{config.BASE_URL}/statistic/{item_id}")

    assert response.status_code == 200
    assert "contacts" in response.json()[0]
    assert "likes" in response.json()[0]
    assert "viewCount" in response.json()[0]

# 8. Получение статистики для несуществующего объявления
def test_get_statistic_for_non_existing_item():
    item_id = "271a2549-611b-4ca4-abf3-eb0bc8838837"  # Заменить на несуществующий itemID
    response = requests.get(f"{config.BASE_URL}/statistic/{item_id}")

    assert response.status_code == 404
    assert response.json()["result"]["message"] == f"statistic {item_id} not found"

# 9. Отправка запроса на несуществующий маршрут
def test_request_without_authorization():
    response = requests.get(f"{config.BASE_URL}/ads")  # Заменить на путь, требующий авторизацию
    assert response.status_code == 404
    assert response.json()["message"] == "route /api/ads not found"

# 10. Отправка запроса POST без тела запроса
def test_post_without_request_body():
    response = requests.post(f"{config.BASE_URL}/item")  # Пустое тело запроса
    assert response.status_code == 400
    assert response.json()["message"] == "invalid content type"

# 11. Попытка создания объявления с уже существующим sellerID
def test_create_item_with_existing_sellerID():
    body = {
        "sellerID": 112277,
        "name": "Another Example Item",
        "price": 1500,
        "description": "Another description of the item"
    }
    response = requests.post(f"{config.BASE_URL}/item", json=body)

    assert response.status_code == 400
    assert response.json()["message"] == "SellerID already exists"

# 12. Отправка запроса с некорректным значением price
def test_create_item_with_invalid_price():
    body = {
        "sellerID": 112277,
        "name": "Item with invalid price",
        "price": -500,
        "description": "This item has an invalid price"
    }
    response = requests.post(f"{config.BASE_URL}/item", json=body)

    assert response.status_code == 400
    assert response.json()["message"] == "Invalid price value"