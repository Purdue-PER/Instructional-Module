from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'download'
urlpatterns = [
    path('', views.download_api, name='main'),
    path('cal/', views.cal_download_view, name='cal'),
    path('user/', views.user_download_view, name='user'),
    path('pre_edu/', views.preEDU_download_view, name='pre_edu'),
    path('pre_log/', views.preLOG_download_view, name='pre_log'),
    path('pre_mouse/', views.preMouse_download_view, name='pre_mouse'),
    path('force_edu/', views.forceEDU_download_view, name='force_edu'),
    path('force_log/', views.forceLOG_download_view, name='force_log'),
    path('force_mouse/', views.forceMouse_download_view, name='force_mouse'),
    path('post_edu/', views.forceEDU_download_view, name='post_edu'),
    path('post_log/', views.forceLOG_download_view, name='post_log'),
    path('post_mouse/', views.forceMouse_download_view, name='post_mouse'),
    path('llm/', views.llm_download_view, name='post_mouse'),
]