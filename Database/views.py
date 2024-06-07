from django.shortcuts import render, redirect
from .forms import MemberForm, MemberPhoneForm, MemberEmailForm, StudentForm, ProfessorForm, TAForm, CourseForm, GroupForm, AssistanceForm, GradeForm, GroupActivitiesForm, InviteRequestForm

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
