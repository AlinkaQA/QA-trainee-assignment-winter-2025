#### bug-тк-02 Создается объявление без sellerID в теле запроса в ручке POST /api/1/item

**Шаги:**  
1. Отправить `POST` запрос без `sellerID`  
2. Проверить, что статус ответа `400 Bad Request`  
3. Проверить сообщение об ошибке  

**Тело запроса:**

```json
{
  "name": "Example Item",
  "price": 1000,
  "description": "Description of the item"
}
```
**Ожидаемый результат:**  
Сервер возвращает 400 Bad Request, сообщение "sellerID is required" 

**Фактический результат:** 
Статус 200 ОК

```json
{
    "status": "Сохранили объявление - 5fc9d4a2-2fa8-4281-a21d-b22faf61720e"
}
```

---

#### bug-тк-09 Сервер возвращает некорректный код в теле ответа при формировании запроса GET https://qa-internship.avito.com/api/1/ads на несуществующий маршрут 

**Шаги:**  
1. Отправить `GET` запрос без авторизационного токена  
2. Проверить, что статус ответа `404Not Found`
3. Проверить сообщение об ошибке

**Запрос:**
GET https://qa-internship.avito.com/api/1/ads 

**Ожидаемый результат:**  
- Сервер возвращает `404Not Found`

```json
{
    "message": "route /api/1/ads not found",
    "code": 404
}
```
**Фактическийт результат:** 

```json
{
    "message": "route /api/1/ads not found",
    "code": 400
}
```
---

#### bug-тк-11 Повторно создается объявление с уже существующим sellerID при отправке запроса POST /api/1/item

**Шаги:**
1. Отправить `POST` запрос с повторяющимся `sellerID`, который уже существует в системе.
2. Проверить, что статус ответа `400 Bad Request`.
3. Проверить сообщение об ошибке, например, "SellerID already exists".

**Тело запроса:**

```json
{
  "sellerID": 112277,
  "name": "Another Example Item",
  "price": 1500,
  "description": "Another description of the item"
}
```

**Ожидаемый результат:**  
Сервер возвращает ошибку с кодом 400 Bad Request и сообщение "SellerID already exists". 

```json
{
    "message": "SellerID already exists",
    "code": 400
}
```
**Фактический результат:**  
Статус 200 ОК

```json
{
    "status": "Сохранили объявление - 352a8177-7200-4703-9005-0d66bd833060"
}
```
---

#### bug-тк-12 Сервер возвращает код 200 ОК при отправка запроса с некорректным значением price в ручке POST https://qa-internship.avito.com/api/1/item

**Шаги:**
1. Отправить `POST` запрос с некорректным значением `price`, например, отрицательным числом или нулем.
2. Проверить, что статус ответа `400 Bad Request`.
3. Проверить сообщение об ошибке, например, "Invalid price value".

**Тело запроса:**
```json
{
  "sellerID": 112277,
  "name": "Item with invalid price",
  "price": -500,
  "description": "This item has an invalid price"
}
```

**Ожидаемый результат:**  

Сервер возвращает ошибку с кодом 400 Bad Request и сообщение "Invalid price value".

```json
{
    "message": "Invalid price value",
    "code": 400
}
```
**Фактический результат:** 
Статус 200 ОК
```json
 {
    "status": "Сохранили объявление - ddd19a53-38ad-4461-bd43-0709331bb3d3"
}
```
---
