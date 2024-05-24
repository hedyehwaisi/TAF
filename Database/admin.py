from django.contrib import admin
from .models import User, Student, Department, Professor

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Professor)
