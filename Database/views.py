from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import MemberForm, MemberPhoneForm, MemberEmailForm, StudentForm, ProfessorForm, TAForm, CourseForm, \
    GroupForm, AssistanceForm, GradeForm, GroupActivitiesForm, InviteRequestForm, MemberSearchForm, PhoneFormSet
from .models import Member, Student, TA, Professor, Course, Group, Assistance, Grade, InviteRequest, MemberPhone, MemberEmail
from django.db.models import Q
from django.db import IntegrityError



# Homepage view
def homepage(request):
    return render(request, 'homepage.html')

def lists(request):
    return render(request, 'lists.html')

def create_page(request):
    return render(request, 'create.html')


def create_member(request):
    if request.method == 'POST':
        member_form = MemberForm(request.POST)
        email_form = MemberEmailForm(request.POST)
        phone_formset = PhoneFormSet(request.POST, queryset=MemberPhone.objects.none())

        if member_form.is_valid() and email_form.is_valid() and phone_formset.is_valid():
            member = member_form.save()
            email = email_form.save(commit=False)
            email.member = member
            email.save()

            for phone_form in phone_formset:
                try:
                    phone = phone_form.save(commit=False)
                    phone.member = member
                    phone.save()
                except IntegrityError:
                    # Handle the case where the phone number already exists
                    # For example, you can add an error to the formset
                    phone_form.add_error(None, "Phone number already exists.")
                    # Rollback the transaction or handle the error as needed

            if member.role == 'student':
                return redirect('create_student', member_id=member.member_id)
            elif member.role == 'ta':
                return redirect('create_ta', member_id=member.member_id)
            elif member.role == 'professor':
                return redirect('create_professor', member_id=member.member_id)
    else:
        member_form = MemberForm()
        email_form = MemberEmailForm()
        phone_formset = PhoneFormSet(queryset=MemberPhone.objects.none())

    return render(request, 'create/create_member.html', {
        'member_form': member_form,
        'email_form': email_form,
        'phone_formset': phone_formset
    })




# def edit_member(request, member_id):
#     member = get_object_or_404(Member, pk=member_id)

#     if request.method == 'POST':
#         form = MemberForm(request.POST, instance=member)

#         if form.is_valid():
#             mem = form.save()

#             if member.role == 'student':
#                 stu = get_object_or_404(Student, member = member.member_id)
#                 stu.delete()
#             elif member.role == 'professor':
#                 prof = get_object_or_404(Professor, member = member.member_id)
#                 prof.delete()
#             elif member.role == 'ta':
#                 ta = get_object_or_404(TA, member = member.member_id)
#                 ta.delete()

#             if mem.role == 'student':
#                 return redirect('create_student', member_id=member.member_id)
#             elif mem.role == 'ta':
#                 return redirect('create_ta', member_id=member.member_id)
#             elif mem.role == 'professor':
#                 return redirect('create_professor', member_id=member.member_id)



#             return redirect('members')
#     else:
#         form = MemberForm(instance=member)
#     return render(request, 'edit/edit_member.html', {'form': form, 'member': member})

def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()

            return redirect('members')
    else:
        form = MemberForm(instance=member)
    return render(request, 'edit/edit_member.html', {'form': form, 'member': member})



def edit_student(request, member_id):
    member = get_object_or_404(Student, pk=member_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = StudentForm(instance=member)
    return render(request, 'edit/edit_student.html', {'form': form, 'member': member})



def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('members')
    return render(request, 'delete/delete_member.html', {'member': member})


def members(request):
    form = MemberSearchForm(request.GET)
    members = Member.objects.all()
    phones = MemberPhone.objects.all()
    emails = MemberEmail.objects.all()
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        member_id = form.cleaned_data.get('member_id')

        if first_name:
            members = members.filter(first_name__icontains=first_name)
        if last_name:
            members = members.filter(last_name__icontains=last_name)
        if member_id:
            members = members.filter(member_id=member_id)
    
    return render(request, 'list/members.html', {'members': members, 'form': form, 'phones': phones, 'emails': emails})


def create_student(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.member = member
            student.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'create/create_student.html', {'form': form})


def students(request):
    students = Student.objects.all()
    return render(request, 'list/students.html', {'students': students})


def create_ta(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = TAForm(request.POST)
        if form.is_valid():
            ta = form.save(commit=False)
            ta.member = member
            ta.save()
            return redirect('tas')
    else:
        form = TAForm()
    return render(request, 'create/create_ta.html', {'form': form})

def tas(request):
    tas = TA.objects.all()
    return render(request, 'list/tas.html', {'tas': tas})


def create_professor(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.member = member
            professor.save()
            return redirect('professors')
    else:
        form = ProfessorForm()
    return render(request, 'create/create_professor.html', {'form': form})

def professors(request):
    professors = Professor.objects.all()
    return render(request, 'list/professors.html', {'professors': professors})




# Course views
def courses(request):
    courses = Course.objects.all()
    return render(request, 'list/courses.html', {'courses': courses})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'create/create_course.html', {'form': form})


def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit/edit_course.html', {'form': form, 'course': course})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses')
    return render(request, 'delete/delete_course.html', {'course': course})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'list/courses.html', {'courses': courses})


# Group views
def groups(request):
    groups = Group.objects.all()
    return render(request, 'list/groups.html', {'groups': groups})


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    else:
        form = GroupForm()
    return render(request, 'create/create_group.html', {'form': form})


def edit_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups')
    else:
        form = GroupForm(instance=group)
    return render(request, 'edit/edit_group.html', {'form': form, 'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('groups')
    return render(request, 'delete/delete_group.html', {'group': group})


# Assistance views
def assistances(request):
    assistances = Assistance.objects.all()
    return render(request, 'list/assistances.html', {'assistances': assistances})


def create_assistance(request):
    if request.method == 'POST':
        form = AssistanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assistances')
    else:
        form = AssistanceForm()
    return render(request, 'create/create_assistance.html', {'form': form})


def edit_assistance(request, assistance_id):
    assistance = get_object_or_404(Assistance, pk=assistance_id)
    if request.method == 'POST':
        form = AssistanceForm(request.POST, instance=assistance)
        if form.is_valid():
            form.save()
            return redirect('assistances')
    else:
        form = AssistanceForm(instance=assistance)
    return render(request, 'edit/edit_assistance.html', {'form': form, 'assistance': assistance})


def delete_assistance(request, assistance_id):
    assistance = get_object_or_404(Assistance, pk=assistance_id)
    if request.method == 'POST':
        assistance.delete()
        return redirect('assistances')
    return render(request, 'delete/delete_assistance.html', {'assistance': assistance})


# Grade views
def grades(request):
    grades = Grade.objects.all()
    return render(request, 'list/grades.html', {'grades': grades})


def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades')
    else:
        form = GradeForm()
    return render(request, 'create/create_grade.html', {'form': form})


def edit_grade(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'edit/edit_grade.html', {'form': form, 'grade': grade})


def delete_grade(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == 'POST':
        grade.delete()
        return redirect('grades')
    return render(request, 'delete/delete_grade.html', {'grade': grade})


# RequestInvite views
def invite_requests(request):
    invite_requests = InviteRequest.objects.all()
    return render(request, 'list/invite_requests.html', {'invite_requests': invite_requests})


def create_invite_request(request):
    if request.method == 'POST':
        form = InviteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invite_requests')
    else:
        form = InviteRequestForm()
    return render(request, 'create/create_invite_request.html', {'form': form})


def edit_invite_request(request, invite_request_id):
    invite_request = get_object_or_404(InviteRequest, pk=invite_request_id)
    if request.method == 'POST':
        form = InviteRequestForm(request.POST, instance=invite_request)
        if form.is_valid():
            form.save()
            return redirect('invite_requests')
    else:
        form = InviteRequestForm(instance=invite_request)
    return render(request, 'edit/edit_invite_request.html', {'form': form, 'invite_request': invite_request})


def delete_invite_request(request, invite_request_id):
    invite_request = get_object_or_404(InviteRequest, pk=invite_request_id)
    if request.method == 'POST':
        invite_request.delete()
        return redirect('invite_requests')
    return render(request, 'delete/delete_invite_request.html', {'invite_request': invite_request})



# # Group Activities views
# def create_group_activities(request):
#     if request.method == 'POST':
#         form = GroupActivitiesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('group_activities_list')
#     else:
#         form = GroupActivitiesForm()
#     return render(request, 'create_group_activities.html', {'form': form})
#
#
# # Invite Request views
# def create_invite_request(request):
#     if request.method == 'POST':
#         form = InviteRequestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('invite_request_list')
#     else:
#         form = InviteRequestForm()
#     return render(request, 'create_invite_request.html', {'form': form})
