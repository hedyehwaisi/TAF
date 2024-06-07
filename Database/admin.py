from django.contrib import admin
from .models import (Assistance, Course, Grade, Member, InviteRequest, MemberPhone, MemberEmail,
                     Group, GroupActivities, Professor, Student, TA)

# Register your models here.
admin.site.register(Assistance)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Member)
admin.site.register(InviteRequest)
admin.site.register(MemberPhone)
admin.site.register(MemberEmail)
admin.site.register(Group)
admin.site.register(GroupActivities)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(TA)