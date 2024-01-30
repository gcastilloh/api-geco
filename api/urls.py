from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('obtener-token/', views.obtener_token, name='obtener_token'),
    path('corpus', views.corpus_v0_1, name='corpus_disponibles'),
    path('procesar/<int:corpus_id>', views.procesar, name='procesar_corpus')
]
