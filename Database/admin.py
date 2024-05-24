from django.contrib import admin
from .models import User, Student, Department, Professor, TA, Course, Group, Assistance

admin.site.register(User)
admin.site.register(Department)

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(TA)

admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Assistance)
