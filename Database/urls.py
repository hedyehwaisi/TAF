from django.urls import path
from . import views

urlpatterns = [
    # path('Database/', views.members, name='members'),
    path('', views.members, name='members'),
]
