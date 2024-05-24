from django.urls import path
from . import views

urlpatterns = [
    path('view_professors/', views.view_professors, name='view_professors'),
    # path('view_courses/', views.view_courses, name='view_courses'),
    # path('view_tas/', views.view_tas, name='view_tas'),
    # path('view_students/', views.view_students, name='view_students'),

    path('add_professor/', views.add_professor, name='add_professor'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_ta/', views.add_ta, name='add_ta'),
    path('add_student/', views.add_student, name='add_student'),
    path('success/', views.success, name='success'),
]
