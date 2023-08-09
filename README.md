1. О чем проект:

Проект QRKot — это благотворительный фонд поддержки котиков. 
Фонд собирает пожертвования на различные целевые проекты: 
на медицинское обслуживание нуждающихся хвостатых, на 
обустройство кошачьей колонии в подвале, на корм 
оставшимся без попечения кошкам — на любые цели, 
связанные с поддержкой кошачьей популяции.

2. Стек:

- Python 3.9
- FastAPI 0.78.0
- SQLAlchemy 1.4.36
- Alembic 1.7.7
- Uvicorn 0.17.6

3. Автор:

Никита Федоров (github: https://github.com/oupsfed)

4. Как запустить локально:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:oupsfed/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Заполнить .env файл

```
APP_TITLE=Название приложения
APP_DESCRIPTION=Описание приложения
DATABASE_URL=URL Базы данных
SECRET=секретный код
FIRST_SUPERUSER_EMAIL=email супер пользователя
FIRST_SUPERUSER_PASSWORD=пароль супер пользователя
```

Создать базу данных и таблицы

```commandline
alembic upgrade head
```

Запустить приложение

```commandline
uvicorn app.main:app
```

Зайти на http://localhost:8000/docs и ознакомиться с документацией API

Приятного пользования!
