# Лабораторна робота 6 - FastAPI + JWT Authentication

## Опис
REST API для управління бібліотекою книг з автентифікацією та авторизацією на основі JWT токенів.

## Виконані вимоги

* ✅ Дані зберігаються в MongoDB
* ✅ Використано Motor (async MongoDB driver)
* ✅ Реалізовано JWT автентифікацію (access token)
* ✅ Реалізовано Refresh Token Flow
* ✅ Захищені ендпоінти для books (Token-based authentication)
* ✅ Реєстрація та логін користувачів
* ✅ Хешування паролів (bcrypt)
* ✅ MongoDB та API запускаються через Docker Compose
* ✅ Чиста архітектура (repository + service + schemas)

## Як запустити

```bash
docker compose up -d --build
```

Документація: http://127.0.0.1:8000/docs

## Ендпоінти автентифікації

| Метод | Ендпоінт | Опис |
|-------|----------|------|
| POST | /auth/register | Реєстрація нового користувача |
| POST | /auth/login | Логін, отримання access + refresh токенів |
| POST | /auth/refresh | Оновлення access token через refresh token |

## Ендпоінти книг (потрібна авторизація)

| Метод | Ендпоінт | Опис |
|-------|----------|------|
| POST | /books/ | Додати книгу |
| GET | /books/?limit=10&offset=0 | Отримати книги з пагінацією + фільтрами |
| GET | /books/{book_id} | Отримати книгу за ID |
| DELETE | /books/{book_id} | Видалити книгу |

### Query-параметри для GET /books/
- `limit`, `offset` — пагінація
- `status=available` / `status=issued`
- `author=Шевченко`

## Як користуватись через Swagger UI

1. Зареєструй користувача через `POST /auth/register`
2. Натисни кнопку **Authorize** вгорі сторінки
3. Введи `username` і `password` → натисни **Authorize**
4. Тепер всі запити до `/books/` будуть автоматично з токеном

## Refresh Token Flow

Після логіну отримуєш два токени:
- **access_token** — живе 30 хвилин, використовується для запитів
- **refresh_token** — живе 7 днів, використовується для отримання нового access_token через `POST /auth/refresh`
