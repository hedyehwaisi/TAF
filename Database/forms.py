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
        widgets = {
            'gpa': forms.NumberInput(attrs={'min': 0, 'max': 20}),
        }
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
        widgets = {
            'score': forms.NumberInput(attrs={'min': 0, 'max': 20}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'unit': forms.NumberInput(attrs={'min': 1, 'max': 4}),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'class_addr': forms.NumberInput(attrs={'min': 300, 'max': 320}),
            'semester': forms.NumberInput(attrs={'min': 1, 'max': 2}),
            'year': forms.NumberInput(attrs={'min': 1400, 'max': 1500}),
        }

class AssistanceForm(forms.ModelForm):
    class Meta:
        model = Assistance
        fields = '__all__'
        widgets = {
            'ta_feedback': forms.NumberInput(attrs={'min': 0, 'max': 20}),
        }


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
        widgets = {
            'prof_grade': forms.NumberInput(attrs={'min': 0, 'max': 20}),
            'ta_grade': forms.NumberInput(attrs={'min': 0, 'max': 20}),
            'stu_to_ta_rate': forms.NumberInput(attrs={'min': 0, 'max': 20}),
        }


class GroupActivitiesForm(forms.ModelForm):
    class Meta:
        model = GroupActivities
        fields = '__all__'

class InviteRequestForm(forms.ModelForm):
    class Meta:
        model = InviteRequest
        fields = '__all__'
        widgets = {
            'prof_to_TA_feedback': forms.NumberInput(attrs={'min': 0, 'max': 20}),
        }
        


class MemberSearchForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=False)
    last_name = forms.CharField(label='Last Name', max_length=100, required=False)
    member_id = forms.IntegerField(label='ID', required=False)
    