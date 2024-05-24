# from django.contrib import admin

# # Register your models here.


from django.contrib import admin
from .models import Professor, Course, TA, Student, Enrollment

admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(TA)
admin.site.register(Student)
admin.site.register(Enrollment)