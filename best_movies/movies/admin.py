from django.contrib import admin
from .models import LastRefresh, Movie

admin.site.register(LastRefresh)
admin.site.register(Movie)
