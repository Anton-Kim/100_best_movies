from django.shortcuts import redirect, render
from .models import LastRefresh, Movie
from .funcs import load_films


def index(request):
    """Выгрузка в шаблон 100 лучших фильмов и времени последнего обновления этого списка"""
    movies = Movie.objects.order_by('-rating')[:100]
    is_last_refresh = LastRefresh.objects.filter(id=1).exists()
    last_refresh = LastRefresh.objects.get(id=1) if is_last_refresh else None
    context = {'last_refresh': last_refresh, 'movies': movies, 'is_last_refresh': is_last_refresh}
    return render(request, 'index.html', context)


def refresh(request):
    """Парсинг фильмов, обновление последнего времени обновления"""
    load_films()
    is_last_refresh = LastRefresh.objects.filter(id=1).exists()
    if is_last_refresh:
        LastRefresh.objects.filter(id=1).delete()
    LastRefresh.objects.create(id=1)
    return redirect('/')
