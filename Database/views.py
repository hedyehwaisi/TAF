from django.shortcuts import render, redirect
from .forms import MemberForm, MemberPhoneForm, MemberEmailForm, StudentForm, ProfessorForm, TAForm, CourseForm, GroupForm, AssistanceForm, GradeForm, GroupActivitiesForm, InviteRequestForm
from .models import Member, MemberPhone, MemberEmail, Student, Professor, TA, Course, Group, Assistance, Grade, GroupActivities, InviteRequest


def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'create_member.html', {'form': form})

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

# Repeat for all other forms...


def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})

def member_phone_list(request):
    member_phones = MemberPhone.objects.all()
    return render(request, 'member_phone_list.html', {'member_phones': member_phones})

def member_email_list(request):
    member_emails = MemberEmail.objects.all()
    return render(request, 'member_email_list.html', {'member_emails': member_emails})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'professor_list.html', {'professors': professors})

def ta_list(request):
    tas = TA.objects.all()
    return render(request, 'ta_list.html', {'tas': tas})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def assistance_list(request):
    assistances = Assistance.objects.all()
    return render(request, 'assistance_list.html', {'assistances': assistances})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grade_list.html', {'grades': grades})

def group_activities_list(request):
    group_activities = GroupActivities.objects.all()
    return render(request, 'group_activities_list.html', {'group_activities': group_activities})

def invite_request_list(request):
    invite_requests = InviteRequest.objects.all()
    return render(request, 'invite_request_list.html', {'invite_requests': invite_requests})
