from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listAll/', views.ListAllEmpleados.as_view()),
    path('listArea/<shortname>/', views.ListByArea.as_view()),

   
]
