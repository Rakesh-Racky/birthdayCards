from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('design/', views.design, name="design"),
]
