from django import forms
from .models import Member, MemberPhone, MemberEmail, Student, Professor, TA, Course, Group, Assistance, Grade, GroupActivities, InviteRequest

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class MemberPhoneForm(forms.ModelForm):
    class Meta:
        model = MemberPhone
        fields = '__all__'

class MemberEmailForm(forms.ModelForm):
    class Meta:
        model = MemberEmail
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class TAForm(forms.ModelForm):
    class Meta:
        model = TA
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class AssistanceForm(forms.ModelForm):
    class Meta:
        model = Assistance
        fields = '__all__'

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

class GroupActivitiesForm(forms.ModelForm):
    class Meta:
        model = GroupActivities
        fields = '__all__'

class InviteRequestForm(forms.ModelForm):
    class Meta:
        model = InviteRequest
        fields = '__all__'
