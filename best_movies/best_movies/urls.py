from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('', views.index),
    path('refresh/', views.refresh, name='refresh'),
    path('admin/', admin.site.urls),
]
