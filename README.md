# Описание:

Учебный проект по изучению автоматизации создания, управления и разворачивания на сервере сайта с использованием контейнеров.

Сайт предназначен для хранения информации и фотографий котов и кошек :)

# Используемые технологии:

Для создания и управления контейнерами используется [Docker](https://www.docker.com/) с расширением [Compose](https://docs.docker.com/compose/)

Для CI/CD применен [GitHub Actions](https://github.com/features/actions).

## Контейнеры

### Backend

- [Django-3.2](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

В качестве СУБД используется [PostgreSQL-13](https://www.postgresql.org/).

Для создания токенов и аутентификации пользователей применен [djoser](https://djoser.readthedocs.io/). 

### Frontend

- [NodeJS-18](https://nodejs.org)

### Прокси-сервер

- [NGINX](https://nginx.org)

# Запуск проекта:

## Подготовка к запуску:

1. Для запуска проекта необходимо на сервере установить Docker и расширение Docker-Compose.

1. Создать директорию для проекта. Например, kittygram.

1. Скопировать в эту директорию файл docker-compose.production.yml

1. Создать в этой директории файл с настройками .env по примеру файла .env.example

## Запуск:

1. Скачать подготовленные контейнеры:

```bash
sudo docker compose -f docker-compose.production.yml pull
```

1. Перезапустить контейнеры:

```bash
sudo docker compose -f docker-compose.production.yml down
sudo docker compose -f docker-compose.production.yml up -d
```

1. Выполнить создание базы данных:

```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```

1. Выполнить подготовку статики для сайта:

```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```

После запуска сайт доступен по адресу 127.0.0.1:8000 или localhost:8000

## Остановка проекта:

```bash
sudo docker compose -f docker-compose.production.yml down
```

## Обновление:

При необходимости можно обновить запущенные контейнеры повторно выполнив команды из раздела "Запуск".

# Работа с сайтом:

Для использования сайта пользователи должны зарегистрироваться.

## Администрирование:

Создание суперпользователя:

```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
```

Управление пользователями возможно в админ зоне сайта 127.0.0.1:8000/admin/

# Примеры запросов к API:

## Регистрация пользователя:

```
POST /api/users/
```

Тело запроса application/json:

```json
{
  "email": "string",
  "username": "string",
  "password": "string"
}
```

Пример ответа:

HTTP 201 Created
```json
{
    "email": "string",
    "username": "string",
    "id": 0
}
```

## Получить токен:

```
POST /api/token/login/
```

Тело запроса application/json:

```json
{
  "username": "string",
  "password": "string"
}
```

Пример ответа:

HTTP 200 OK
```json
{
    "auth_token": "string"
}
```

## Получить список доступных endpoints:

```
GET /api/
```

Пример ответа:

HTTP 200 OK
```json
{
    "cats": "http://127.0.0.1:8000/api/cats/",
    "achievements": "http://127.0.0.1:8000/api/achievements/"
}
```

## Получение списка котов/кошек:

```
GET /api/cats/
```

Пример ответа:

HTTP 200 OK
```
{
  "count": 0,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 0,
      "name": "string",
      "color": "string",
      "birth_year": integer,
      "achievements": [string],
      "owner": integer,
      "age": integer,
      "image": null,
      "image_url": null
    }
  ]
}
```

## Добавление кота/кошки:

```
POST /api/cats/
```

Тело запроса application/json:

```json
{
  "name": "string",
  "color": "string",
  "birth_year": integer,
  "achievements": [string],
  "owner": integer,
  "age": integer,
  "image": null,
  "image_url": null
}
```

Пример ответа:

HTTP 200 OK
```json
{
  "id": 0,
  "name": "string",
  "color": "string",
  "birth_year": integer,
  "achievements": [string],
  "owner": integer,
  "age": integer,
  "image": null,
  "image_url": null
}
```

# Автор:

Проект создан Паутовым Александром на основе репозитория [yandex-praktikum/kittygram_final](https://github.com/yandex-praktikum/kittygram_final)
