from django import forms
from .models import Professor, Course, TA, Student

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'department']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code', 'professor', 'credits']

class TAForm(forms.ModelForm):
    class Meta:
        model = TA
        fields = ['first_name', 'last_name', 'course']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'courses']
