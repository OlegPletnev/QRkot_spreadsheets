# Отчёт в Google Sheets для QRKot

## Описание
В проекте реализована интеграция Google API (Drive и SpreadSheets) в приложение сбора пожертвований QRKot. Добавлена возможность формирования отчёта в гугл-таблице. В таблице формируется список закрытых проектов, отсортированных по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

## Технологии

- [FastAPI](https://fastapi.tiangolo.com/)
- [FastAPI Users](https://fastapi-users.github.io/fastapi-users/)
- [SQLAlchemy](http://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)

## Запуск
Склонируйте репозиторий  
Создайте и активируйте виртуальное окружение 
```
python -m venv venv
source venv/scripts/activate
```
Активируйте виртуальное окружение  
Установите зависимости 
```
pip install -r requirements.txt
```
Создайте файл .env:
```
APP_TITLE=Благотворительный фонд поддержки котиков QRKot
DESCRIPTION=Сбор пожертвований в целевые проекты на нужды хвостатых
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=SECRET
```
Добавьте в него информацию из JSON-файла о вашем сервисном аккаунте;
```
DATABASE_URL=
FIRST_SUPERUSER_EMAIL=
FIRST_SUPERUSER_PASSWORD=
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
EMAIL=
```
Примените миграции для создания файла БД и таблиц
```
alembic upgrade head
```
Запустите сервер из корневой папки проекта
```
uvicorn app.main:app --reload
```

## REST API
Документация API доступна по адресу: http://localhost:8000/docs