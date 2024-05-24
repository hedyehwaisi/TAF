from django.urls import path
from . import views

urlpatterns = [
    path('add_professor/', views.add_professor, name='add_professor'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_ta/', views.add_ta, name='add_ta'),
    path('add_student/', views.add_student, name='add_student'),
    path('success/', views.success, name='success'),
]
