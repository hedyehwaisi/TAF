from django.contrib import admin
from .models import Member, Student, Department, Professor, TA, Course, Group, Assistance

admin.site.register(Member)
admin.site.register(Department)

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(TA)

admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Assistance)
