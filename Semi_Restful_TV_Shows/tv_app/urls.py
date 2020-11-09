from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.showNew),
    path('shows/new/add', views.create),
    path('shows/<int:num>/edit', views.showEdit),
    path('shows/<int:num>/edit/update', views.update),
    path('shows/<int:num>', views.showShow),
    path('shows/<int:num>/delete', views.showDelete),
]