from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.homepage, name='homepage'),
    path('lists/', views.list_page, name='list_page'),
    path('create/', views.create_page, name='create_page'),
    path('delete/', views.delete_page, name='delete_page'),
    path('edit/', views.edit_page, name='edit_page'),

    # Member URLs
    # path('create_member/', views.create_member, name='create_member'),
    path('members/', views.members, name='members'),
    path('member/', views.member, name='member'),
    path('edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),

    path('lists/member_list/', views.member_list, name='member_list'),
    path('lists/ta_list/', views.ta_list, name='ta_list'),
    path('lists/professor_list/', views.professor_list, name='professor_list'),
    path('lists/student_list/', views.student_list, name='student_list'),
    # path('member_phones/', views.member_phone_list, name='member_phone_list'),
    # path('member_emails/', views.member_email_list, name='member_email_list'),

    # Course URLs
    # path('create_course/', views.create_course, name='create_course'),
    path('courses/', views.courses, name='courses'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),

    path('lists/course_list/', views.course_list, name='course_list'),

    # Group URLs
    # path('create_group/', views.create_group, name='create_group'),
    path('groups/', views.groups, name='groups'),
    path('edit_group/<int:group_id>/', views.edit_group, name='edit_group'),
    path('delete_group/<int:group_id>/', views.delete_group, name='delete_group'),

    path('lists/group_list/', views.group_list, name='group_list'),

    # Assistance URLs
    # path('create_assistance/', views.create_assistance, name='create_assistance'),
    path('assistances/', views.assistances, name='assistances'),
    path('edit_assistance/<int:assistance_id>/', views.edit_assistance, name='edit_assistance'),
    path('delete_assistance/<int:assistance_id>/', views.delete_assistance, name='delete_assistance'),

    # Grade URLs
    # path('create_grade/', views.create_grade, name='create_grade'),
    path('grades/', views.grades, name='grades'),
    path('edit_grade/<int:grade_id>/', views.edit_grade, name='edit_grade'),
    path('delete_grade/<int:grade_id>/', views.delete_grade, name='delete_grade'),

    # Request Invite URLs
    # path('create_invite_request/', views.create_invite_request, name='create_request_invite'),
    path('invite_request/', views.invite_requests, name='invite_requests'),
    path('edit_invite_request/<int:invite_request_id>/', views.edit_invite_request, name='edit_invite_request'),
    path('delete_invite_request/<int:invite_request_id>/', views.delete_invite_request, name='delete_invite_request'),

    # path('create_member/', views.create_member, name='create_member'),
    # path('members/', views.members, name='members'),
    # path('members/<int:member_id>/', views.member, name='member'),
    path('create_student/<int:member_id>/', views.create_student, name='create_student'),
    path('create_ta/<int:member_id>/', views.create_ta, name='create_ta'),
    path('create_professor/<int:member_id>/', views.create_professor, name='create_professor'),

    # path('', views.homepage, name='homepage'),
    path('create/', views.create_page, name='create_page'),
    path('create/member/', views.create_member, name='create_member'),
    path('create/course/', views.create_course, name='create_course'),
    path('create/group/', views.create_group, name='create_group'),
    path('create/grade/', views.create_grade, name='create_grade'),
    path('create/assistance/', views.create_assistance, name='create_assistance'),
    path('create/invite_request/', views.create_invite_request, name='create_invite_request'),
    # path('lists/', views.lists_page, name='lists_page'),
    # Add URLs for other actions (delete, edit, etc.) as needed
]