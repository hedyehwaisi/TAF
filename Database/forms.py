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
        fields = ('gpa', 'major', 'entry_year')
        # widgets = {'member': forms.HiddenInput()}
        # exclude = ['member']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        exclude = ['member']

class TAForm(forms.ModelForm):
    class Meta:
        model = TA
        fields = '__all__'
        exclude = ['member']

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


class MemberSearchForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=False)
    last_name = forms.CharField(label='Last Name', max_length=100, required=False)
    member_id = forms.IntegerField(label='ID', required=False)
