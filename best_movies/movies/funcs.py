import requests
import re
from django.core.files import File
from io import BytesIO
from .models import Movie


def load_films():
    """Сбор информации о кино с сайта, её запись в БД, скачивание картинок к новым фильмам в папку
    best_movies/images/. У имеющихся в БД фильмов обновление только рейтинга, добавление новых фильмов в БД."""
    url = 'https://www.kinopoisk.ru/top/navigator/order/ex_rating/perpage/100/'
    st_accept = 'text/html'
    st_useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'
    headers = {'Accept': st_accept, 'User-Agent': st_useragent}
    data = requests.get(url, headers=headers)
    for movie in re.findall(r'item _NO_HIGHLIGHT_([\s\S]*?)myVote', data.text):
        poster_url = re.search(r'src=\"(.*?)\" title=\"/ima', movie).group(1)
        name = re.search(r'class=\"name\">([\s\S]*?)</a>', movie).group(1).split('">')[1].replace('&nbsp;', ' ')
        try_director = re.search(r'реж.([\s\S]*?)</a>', movie)
        director = try_director.group(1).split('">')[1] if try_director else ''
        try_year = re.search(r'<span>([\s\S]*?)<nobr>', movie)
        str_year = re.search(r'\((.*?)\)', try_year.group(1)).group(1) if try_year else None
        year = str_year.split(' ')[0] if str_year else ''
        genre = re.search(r'\((.*?)\)', re.search(r'<br([\s\S]*?)</span>', movie).group(1)).group(1)
        rating = float(re.search(r'IMDb: (.*?)<span>', movie).group(1))
        if Movie.objects.filter(name=name).exists():
            m = Movie.objects.get(name=name)
            m.rating = rating
        else:
            Movie.objects.create(name=name, director=director, year=year, genre=genre, rating=rating)
            file_name = poster_url.split('/')[-1]
            resp = requests.get(poster_url)
            fp = BytesIO()
            fp.write(resp.content)
            m = Movie.objects.get(name=name)
            m.poster.save(file_name, File(fp))
