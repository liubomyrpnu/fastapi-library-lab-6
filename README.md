# Лабораторна робота 4 - FastAPI + MongoDB

## Опис
REST API для управління бібліотекою книг з використанням **MongoDB** та **Limit-Offset пагінації**.

### Виконані вимоги
- ✅ Дані зберігаються в **MongoDB**
- ✅ Використано **Motor** (async MongoDB driver)
- ✅ Реалізовано **Limit-Offset пагінацію**
- ✅ MongoDB запускається через Docker Compose
- ✅ Чиста архітектура (repository + service + schemas)
- ✅ Повний CRUD

## Як запустити

```powershell
docker compose up -d --build

Документація: http://127.0.0.1:8000/docs

Основні ендпоінти
Метод,Ендпоінт,Опис
POST,/books/,Додати книгу
GET,/books/?limit=10&offset=0,Отримати книги з пагінацією + фільтрами
GET,/books/{book_id},Отримати книгу за ID
DELETE,/books/{book_id},Видалити книгу

Query-параметри для GET /books/:
limit, offset — пагінація
status=available / status=issued
author=Шевченко