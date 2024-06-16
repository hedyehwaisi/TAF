from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.homepage, name='homepage'),
    path('lists/', views.lists, name='lists'),
    path('create/', views.create_page, name='create_page'),

    # Member URLs
    path('lists/members/', views.members, name='members'),
    path('edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),

    path('lists/tas/', views.tas, name='tas'),
    path('lists/professors/', views.professors, name='professors'),
    path('lists/students/', views.students, name='students'),
    # path('member_phones/', views.member_phone_list, name='member_phone_list'),
    # path('member_emails/', views.member_email_list, name='member_email_list'),

    # Course URLs
    # path('create_course/', views.create_course, name='create_course'),
    path('lists/courses/', views.courses, name='courses'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),

    # Group URLs
    # path('create_group/', views.create_group, name='create_group'),
    path('lists/groups/', views.groups, name='groups'),
    path('edit_group/<int:group_id>/', views.edit_group, name='edit_group'),
    path('delete_group/<int:group_id>/', views.delete_group, name='delete_group'),

    # Assistance URLs
    # path('create_assistance/', views.create_assistance, name='create_assistance'),
    path('lists/assistances/', views.assistances, name='assistances'),
    path('edit_assistance/<int:assistance_id>/', views.edit_assistance, name='edit_assistance'),
    path('delete_assistance/<int:assistance_id>/', views.delete_assistance, name='delete_assistance'),

    # Grade URLs
    # path('create_grade/', views.create_grade, name='create_grade'),
    path('lists/grades/', views.grades, name='grades'),
    path('edit_grade/<int:grade_id>/', views.edit_grade, name='edit_grade'),
    path('delete_grade/<int:grade_id>/', views.delete_grade, name='delete_grade'),

    # Request Invite URLs
    # path('create_invite_request/', views.create_invite_request, name='create_request_invite'),
    path('lists/invite_request/', views.invite_requests, name='invite_requests'),
    path('edit_invite_request/<int:invite_request_id>/', views.edit_invite_request, name='edit_invite_request'),
    path('delete_invite_request/<int:invite_request_id>/', views.delete_invite_request, name='delete_invite_request'),

    # path('create_member/', views.create_member, name='create_member'),
    # path('members/', views.members, name='members'),
    # path('members/<int:member_id>/', views.member, name='member'),
    path('create_student/<int:member_id>/', views.create_student, name='create_student'),
    path('create_ta/<int:member_id>/', views.create_ta, name='create_ta'),
    path('create_professor/<int:member_id>/', views.create_professor, name='create_professor'),

    # path('', views.homepage, name='homepage'),
    path('create/member/', views.create_member, name='create_member'),
    path('create/course/', views.create_course, name='create_course'),
    path('create/group/', views.create_group, name='create_group'),
    path('create/grade/', views.create_grade, name='create_grade'),
    path('create/assistance/', views.create_assistance, name='create_assistance'),
    path('create/invite_request/', views.create_invite_request, name='create_invite_request'),
    # path('lists/', views.lists_page, name='lists_page'),
    # Add URLs for other actions (delete, edit, etc.) as needed
]