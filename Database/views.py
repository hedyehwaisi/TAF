from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import MemberForm, MemberPhoneForm, MemberEmailForm, StudentForm, ProfessorForm, TAForm, CourseForm, \
    GroupForm, AssistanceForm, GradeForm, GroupActivitiesForm, InviteRequestForm
from .models import Member, Student, TA, Professor, Course, Group, Assistance, Grade, InviteRequest


# def index(request):
#     return render(request, 'index.html')

# Homepage view
def homepage(request):
    return render(request, 'homepage.html')


def list_page(request):
    # Your logic to retrieve and display lists
    return render(request, 'list_page.html')


def create_page(request):
    return render(request, 'create_page.html')


# def delete_page(request):
#     # Your logic for deleting items
#     context = {
#         # Assuming 'member_id' is None if not available
#         'member_id': None,  # or any default value you prefer
#         'course_id': None,
#         'group_id': None,
#         'grade_id': None,
#         'assistance_id': None,
#         'invite_request_id': None
#     }
#     return render(request, 'delete_page.html', context)


def delete_page(request, member_id=None, course_id=None, group_id=None, grade_id=None, assistance_id=None,
                invite_request_id=None):
    # Create links for each delete action
    delete_links = {
        'delete_member': reverse('delete_member', args=(member_id,)) if member_id else None,
        'delete_course': reverse('delete_course', args=(course_id,)) if course_id else None,
        'delete_group': reverse('delete_group', args=(group_id,)) if group_id else None,
        'delete_grade': reverse('delete_grade', args=(grade_id,)) if grade_id else None,
        'delete_assistance': reverse('delete_assistance', args=(assistance_id,)) if assistance_id else None,
        'delete_invite_request': reverse('delete_invite_request',
                                         args=(invite_request_id,)) if invite_request_id else None,
    }
    return render(request, 'delete_page.html', {'delete_links': delete_links})


def edit_page(request):
    # Your logic for editing items
    return render(request, 'edit_page.html')


# Member views
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


def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm(instance=member)
    return render(request, 'edit_member.html', {'form': form, 'member': member})


def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('members')
    return render(request, 'delete_member.html', {'member': member})


def members(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})


def member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'member.html', {'member': member})


def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})


# def member_phone_list(request):
#     member_phones = MemberPhone.objects.all()
#     return render(request, 'member_phone_list.html', {'member_phones': member_phones})

# def member_email_list(request):
#     member_emails = MemberEmail.objects.all()
#     return render(request, 'member_email_list.html', {'member_emails': member_emails})

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


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


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

def ta_list(request):
    tas = TA.objects.all()
    return render(request, 'ta_list.html', {'tas': tas})


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

def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'professor_list.html', {'professors': professors})


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


# Course views
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})


def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form, 'course': course})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courses')
    return render(request, 'delete_course.html', {'course': course})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


# Group views
def groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})


def edit_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups')
    else:
        form = GroupForm(instance=group)
    return render(request, 'edit_group.html', {'form': form, 'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('groups')
    return render(request, 'delete_group.html', {'group': group})


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

# Assistance views
def assistances(request):
    assistances = Assistance.objects.all()
    return render(request, 'assistances.html', {'assistances': assistances})


def create_assistance(request):
    if request.method == 'POST':
        form = AssistanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assistances')
    else:
        form = AssistanceForm()
    return render(request, 'create_assistance.html', {'form': form})


def edit_assistance(request, assistance_id):
    assistance = get_object_or_404(Assistance, pk=assistance_id)
    if request.method == 'POST':
        form = AssistanceForm(request.POST, instance=assistance)
        if form.is_valid():
            form.save()
            return redirect('assistances')
    else:
        form = AssistanceForm(instance=assistance)
    return render(request, 'edit_assistance.html', {'form': form, 'assistance': assistance})


def delete_assistance(request, assistance_id):
    assistance = get_object_or_404(Assistance, pk=assistance_id)
    if request.method == 'POST':
        assistance.delete()
        return redirect('assistances')
    return render(request, 'delete_assistance.html', {'assistance': assistance})


# Grade views
def grades(request):
    grades = Grade.objects.all()
    return render(request, 'grades.html', {'grades': grades})


def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades')
    else:
        form = GradeForm()
    return render(request, 'create_grade.html', {'form': form})


def edit_grade(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'edit_grade.html', {'form': form, 'grade': grade})


def delete_grade(request, grade_id):
    grade = get_object_or_404(Grade, pk=grade_id)
    if request.method == 'POST':
        grade.delete()
        return redirect('grades')
    return render(request, 'delete_grade.html', {'grade': grade})


# RequestInvite views
def invite_requests(request):
    invite_requests = InviteRequest.objects.all()
    return render(request, 'invite_requests.html', {'invite_requests': invite_requests})


def create_invite_request(request):
    if request.method == 'POST':
        form = InviteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invite_requests')
    else:
        form = InviteRequestForm()
    return render(request, 'create_invite_request.html', {'form': form})


def edit_invite_request(request, invite_request_id):
    invite_request = get_object_or_404(InviteRequest, pk=invite_request_id)
    if request.method == 'POST':
        form = InviteRequestForm(request.POST, instance=invite_request)
        if form.is_valid():
            form.save()
            return redirect('invite_requests')
    else:
        form = InviteRequestForm(instance=invite_request)
    return render(request, 'edit_invite_request.html', {'form': form, 'invite_request': invite_request})


def delete_invite_request(request, invite_request_id):
    invite_request = get_object_or_404(InviteRequest, pk=invite_request_id)
    if request.method == 'POST':
        invite_request.delete()
        return redirect('invite_requests')
    return render(request, 'delete_invite_request.html', {'invite_request': invite_request})

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
