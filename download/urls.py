from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'download'
urlpatterns = [
    path('', views.download_view, name='dl'),
]