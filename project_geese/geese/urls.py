from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('all/', views.all),
    path('add/', views.add),
    path('delete/', views.delete),
    path('update/', views.update),
    path('sttchck/<int:idtf>/', views.sttchck),
    path('passchck/', views.passchck)
]