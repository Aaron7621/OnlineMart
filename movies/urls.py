from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us),
    path('movies/', views.movies),
]