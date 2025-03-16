# SmartFridge, Back-end part

![mosh-image](https://predprof.olimpiada.ru/images/logo-predporf.svg)

**Back-end** Проект заключительного этапа Московской Предпрофессиональной Олимпиады

> Исходиники: [Git репозиторий](https://github.com/vetkas2023/smart_fridge_frontend)

## Описание

### О проекте

> [!NOTE]
> ТУТУТ

---

### Описание приложения

Представляет из себя .

## Начало работы

### Зависимости

_См. [`pyproject.toml`](https://github.com/HayKor/smart_fridge_backend/blob/main/pyproject.toml)_

- **Lang**: Python 3.12+
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [Pydantic](https://docs.pydantic.dev/latest/), [PyQt6](https://doc.qt.ioqtforpython-6/).  
- **ASGI**: Uvicorn
- **Data management**: SQLite
- **Dependency management**: [Poetry](https://python-poetry.org/docs/)

### Установка

**Предусловие**: python, poetry

##### 2. Установка зависимостей с `poetry`

```shell
poetry install
```

### Запуск

**Предусловие**: python, poetry, alembic, _make_\*

_\*: необязательно_

#### Local development среда

##### 1. Настройка `.env`

Создайте файл `.env` (см. [`.env.example`](https://github.com/))

```
#.env
DATABASE__URL=sqlite+aiosqlite:///database.db
```

##### 2. Запуск dev среды (database)

Применяем миграции к базе данных

```shell
alembic upgrade head
```

##### 3. API-сервис

```shell
uvicorn app.main:app --reload
```

API-документация будет доступна по адресу

```shell
http://localhost:8080/docs
```

##### 4. UI-интерфейс

```shell
python client/main.py
```

#### Production среда

...coming soon

## Помощь



## Авторы

- [Артур Багинян](https://github.com/HayKor/)
- [Гриценко Владислав](https://github.com/Gr1zee)
- [Гришин Илья](https://github.com/ilyaaadfb)
- [Светлана Сердюк](https://github.com/vetkas2023) - фронт-енд (см. [выше](./README.md#smartfridge-back-end-part))

## Ссылки

- [awesome-readme](https://github.com/matiassingers/awesome-readme)
