# Сервис услуг

## Стек

`Python`, `sqlalchemy`, `Pydantic`, `alembic`, `fastapi`

## Описание сервиса

Сервис позволяет управлять услугами которые предоставляют почтовые отделения.

## Структура проекта

```
services/
├── Dockerfile
├── Readme.md
├── .env.example            # Пример конфигурации для .env
├── alembic/
├── alembic.ini
├── src/                    # Директория с проектом
│   ├── helpers/            # Сервисный слой
│   ├── routers/            # Директория с HTTP эндпоинтами
│   ├── migrations/         # Настройка миграций
│   ├── models/             # Директория с моделями БД
│   ├── schemas/            # Директория с схемами валидации
│   ├── main.py             # Точка входа
│   ├── config.py           # Файл с конфигом
│   ├── database.py         # Файл с конфигурацией подключения БД
├── docker-compose.yml
└── requirements.txt        # python-пакеты
```

## Развертывание проекта

1. Склонируйте репозиторий

```bash
git clone https://github.com/mzhn-fsp-dnr/offices.git
```

2. Настройте приложение путем редактирования `.env` файла. Пример расположен в `.env.example`

3. Запустите приложение в Docker

```bash
docker compose up --build
```
