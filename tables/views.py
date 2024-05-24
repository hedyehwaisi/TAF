# from django.shortcuts import render

# # Create your views here.

from django.shortcuts import render, redirect
from .forms import ProfessorForm, CourseForm, TAForm, StudentForm, Professor, Course, TA, Student


def add_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProfessorForm()
    return render(request, 'add_professor.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def add_ta(request):
    if request.method == 'POST':
        form = TAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TAForm()
    return render(request, 'add_ta.html', {'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def view_professors(request):
    professors = Professor.objects.all()
    return render(request, 'view_professors.html', {'professors': professors})

def view_courses(request):
    courses = Course.objects.all()
    return render(request, 'view_courses.html', {'courses': courses})

def view_tas(request):
    tas = TA.objects.all()
    return render(request, 'view_tas.html', {'tas': tas})

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})
