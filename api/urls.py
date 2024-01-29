from django.urls import path
from . import views

urlpatterns = [
    path('corpus', views.corpus_v0_1, name='corpus_disponibles'),
]