from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm, MemberPhoneForm, MemberEmailForm, StudentForm, ProfessorForm, TAForm, CourseForm, \
    GroupForm, AssistanceForm, GradeForm, GroupActivitiesForm, InviteRequestForm
from .models import Member, Student, TA, Professor


def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()  # Save the member to generate the id
            # Redirect to the appropriate role form
            if member.role == 'student':
                return redirect('create_student', member_id=member.member_id)
            elif member.role == 'ta':
                return redirect('create_ta', member_id=member.member_id)
            elif member.role == 'professor':
                return redirect('create_professor', member_id=member.member_id)
    else:
        form = MemberForm()
    return render(request, 'create_member.html', {'form': form})


# return redirect('member_list')

def index(request):
    return render(request, 'index.html')


def members(request):
    all_members = Member.objects.all()
    return render(request, 'members.html', {'members': all_members})


def member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'member.html', {'member': member})


# return redirect('member_list')

def create_student(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.member = member
            student.save()
            return redirect('members')
    else:
        form = StudentForm()
    return render(request, 'new_student.html', {'form': form})


def create_ta(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = TAForm(request.POST)
        if form.is_valid():
            ta = form.save(commit=False)
            ta.member = member
            ta.save()
            return redirect('members')
    else:
        form = TAForm()
    return render(request, 'new_ta.html', {'form': form})


def create_professor(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.member = member
            professor.save()
            return redirect('members')
    else:
        form = ProfessorForm()
    return render(request, 'new_professor.html', {'form': form})


# Similarly, create views for other forms
# Example for MemberPhone
def create_member_phone(request):
    if request.method == 'POST':
        form = MemberPhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_phone_list')
    else:
        form = MemberPhoneForm()
    return render(request, 'create_member_phone.html', {'form': form})


def create_member_email(request):
    if request.method == 'POST':
        form = MemberEmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_email_list')
    else:
        form = MemberEmailForm()
    return render(request, 'create_member_email.html', {'form': form})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})


def create_assistance(request):
    if request.method == 'POST':
        form = AssistanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assistance_list')
    else:
        form = AssistanceForm()
    return render(request, 'create_assistance.html', {'form': form})


def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'create_grade.html', {'form': form})


def create_group_activities(request):
    if request.method == 'POST':
        form = GroupActivitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_activities_list')
    else:
        form = GroupActivitiesForm()
    return render(request, 'create_group_activities.html', {'form': form})


def create_invite_request(request):
    if request.method == 'POST':
        form = InviteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invite_request_list')
    else:
        form = InviteRequestForm()
    return render(request, 'create_invite_request.html', {'form': form})
