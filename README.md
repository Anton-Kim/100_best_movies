# 100_best_movies
100_best_movies - одностраничный сайт на Django, собирающий информацию о 100 лучших фильмах.

![site](https://github.com/user-attachments/assets/02588c03-0042-480f-94fa-c7ae1fae60a8)

![db](https://github.com/user-attachments/assets/7e42a80c-87a9-4155-8d1f-3f8a18a89d61)


### Особенности:
- парсинг фильмов из известного каталога;
- сохранение в БД названия фильма, режиссера, года выпуска, жанра, рейтинга IMDb и маленького постера фильма на сервере;
- первый запуск может потребовать определенного времени для обработки всех фильмов, их занесения в БД и сохранения постеров к фильмам.
- код написан на Python 3.11

### Запуск проекта на локальной машине:

Клонировать репозиторий:
```
git clone https://github.com/Anton-Kim/100_best_movies.git
```
Cоздать виртуальное окружение в папке с репозиторием:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
source venv/scripts/activate
```
Обновить PIP и установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Перейти в папку best_movies, содержащую файл manage.py:
```
cd best_movies/
```
Создать и запустить миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Запустить проект на локальной машине или на сервере:
```
python manage.py runserver
```
