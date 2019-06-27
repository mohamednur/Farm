from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('help/', views.help, name='help'),
    path('index', views.index, name='index')

]
