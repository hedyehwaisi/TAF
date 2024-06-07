from django.urls import path
from . import views

urlpatterns = [
    path('create_member/', views.create_member, name='create_member'),
    path('', views.members, name='index'),  # Add this to handle the root URL
    path('members/', views.members, name='members'),
    path('members/<int:member_id>/', views.member, name='member'),
    path('create_student/<int:member_id>/', views.create_student, name='create_student'),
    path('create_ta/<int:member_id>/', views.create_ta, name='create_ta'),
    path('create_professor/<int:member_id>/', views.create_professor, name='create_professor'),
]