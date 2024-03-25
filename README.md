# hrspace-request-builder-backend
[![CI/CD](https://github.com/hrspace-request-builder/hrspace-request-builder-backend/actions/workflows/main.yml/badge.svg)](https://github.com/hrspace-request-builder/hrspace-request-builder-backend/actions/workflows/main.yml)

Проект развернут на удаленном сервере по адресу  http://185.221.162.231:81
  - админ панель доступна по адресу http://185.221.162.231/admin
  - Swagger доступен по адресу http://185.221.162.231/docs
  - Redoc доступен по адресу http://185.221.162.231/redoc

<br>

## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка приложения](#установка-приложения)
- [Запуск приложения](#запуск-приложения)
- [Удаление приложения](#удаление-приложения)
- [Авторы](#авторы)

<br>

## Технологии
<details><summary>Подробнее</summary><br>

[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?logo=Pydantic)](https://docs.pydantic.dev/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)
[![asyncpg](https://img.shields.io/badge/-asyncpg-464646?logo=PostgreSQL)](https://pypi.org/project/asyncpg/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-blue?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Uvicorn](https://img.shields.io/badge/-Uvicorn-464646?logo=Uvicorn)](https://www.uvicorn.org/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![pre-commit](https://img.shields.io/badge/-pre--commit-464646?logo=pre-commit)](https://pre-commit.com/)

[⬆️Оглавление](#оглавление)

</details>

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

[⬆️Оглавление](#оглавление)

<br>

## Запуск приложения:

1. Из корневой директории проекта выполните команду:
```bash
docker compose -f docker/docker-compose.yml --env-file .env up -d --build
```
  Проект будет развернут в docker-контейнерах по адресу http://localhost:81

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

[⬆️Оглавление](#оглавление)

<br>

## Удаление приложения:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr hrspace-request-builder-backend
```

[⬆️Оглавление](#оглавление)

<br>

## Авторы:
- [Aleksei Proskuriakov](https://github.com/alexpro2022)
- [Bair Erendzhenov](https://github.com/ErendzhenovBair)
- [Stanislav Zatushevskii](https://github.com/stas-zatushevskii)
<br>
[⬆️В начало](#hrspace-request-builder-backend)
