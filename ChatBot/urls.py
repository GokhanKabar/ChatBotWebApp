from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatApp, name="ChatApp"),
    path('send/', views.SendMessage, name='sendMessage'),
    path('getMessages/', views.getMessages, name='getMessages'),
    path('reset/', views.Reset, name='reset'),
]
