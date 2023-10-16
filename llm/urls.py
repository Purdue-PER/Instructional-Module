from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.llm_landing,name='force')
]