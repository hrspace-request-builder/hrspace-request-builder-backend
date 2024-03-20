# hrspace-request-builder-backend
[![CI/CD](https://github.com/hrspace-request-builder/hrspace-request-builder-backend/actions/workflows/main.yml/badge.svg)](https://github.com/hrspace-request-builder/hrspace-request-builder-backend/actions/workflows/main.yml)

Проект развернут на удаленном сервере по адресу  http://185.221.162.231/hrspace:
  - админ панель доступна по адресу http://185.221.162.231/admin
  - Swagger доступен по адресу http://185.221.162.231/docs
  - Redoc доступен по адресу http://185.221.162.231/redoc

<br>

## Установка приложения:

<details><summary>Предварительные условия</summary>

Предполагается, что пользователь установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине. Проверить наличие можно выполнив команды:

```bash
docker --version && docker-compose --version
```
</details>

<br>

Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):

```bash
git clone https://github.com/hrspace-request-builder/hrspace-request-builder-backend.git
cd hrspace-request-builder-backend
cp env_example .env
nano .env
```

<br>

## Запуск приложения:

1. Из корневой директории проекта выполните команду:
```bash
docker compose -f docker/docker-compose.yml --env-file .env up -d --build
```
  Проект будет развернут в docker-контейнерах по адресу http://localhost/hrspace

  Администрирование приложения может быть осуществлено:
  - через Swagger доступный по адресу http://localhost/docs
  - через админ панель по адресу http://localhost/admin

  Техническая документация:
  - Swagger доступен по адресу http://localhost/docs
  - Redoc доступен по адресу http://localhost/redoc

<br>
2. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:

```bash
docker compose -f docker/docker-compose.yml --env-file .env down
```

Если также необходимо удалить том базы данных:
```bash
docker compose -f docker/docker-compose.yml --env-file .env down -v
```

<br>

## Удаление приложения:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr hrspace-request-builder-backend
```
