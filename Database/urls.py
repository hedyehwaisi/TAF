from django.urls import path
from . import views

urlpatterns = [
    path('create_member/', views.create_member, name='create_member'),
    # path('', views.Hello, name='sayhello'),
    
]