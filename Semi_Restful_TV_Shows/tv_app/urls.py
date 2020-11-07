from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.showNew),
    path('shows/edit', views.showEdit),
    path('shows/1', views.showShow),
]