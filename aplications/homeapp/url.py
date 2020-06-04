from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('listaPrueba/', views.ListarPrueba.as_view()),
    path('crearPrueba/', views.PruebaCreateView.as_view()),
]