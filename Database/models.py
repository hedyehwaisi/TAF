from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Member(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    linkedIn_addr = models.URLField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    is_admin = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MemberPhone(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^(09|\+989)\d{9}$',
                                 message="Phone number must be in the format '09xxxxxxxxx' or '+989xxxxxxxxx'.")
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    phone_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.phone_type}: {self.phone}"


class MemberEmail(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    email_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.email_type}: {self.email}"


class Student(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    major = models.CharField(max_length=100)
    entry_year = models.PositiveIntegerField()

    @property
    def computed_id(self):
        return f"{self.member.member_id}01"

    def __str__(self):
        # Safeguard against potential recursive calls
        try:
            return f"Student: {self.member.first_name} {self.member.last_name}, Major: {self.major}, GPA: {self.gpa}, ID: {self.computed_id}"
        except RecursionError:
            return "Professor: Recursion Error"

class Professor(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)
    profRank = models.CharField(max_length=50)
    research_field = models.CharField(max_length=100)

    @property
    def computed_id(self):
        return f"{self.member.member_id}02"

    def __str__(self):
        # Safeguard against potential recursive calls
        try:
            return f"Professor: {self.member.first_name} {self.member.last_name}, Rank: {self.profRank}, Research: {self.research_field}, ID: {self.computed_id}"
        except RecursionError:
            return "Professor: Recursion Error"


class TA(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)

    @property
    def computed_id(self):
        return f"{self.member.member_id}03"
    
    @property
    def score_comuting(self):
        total_score = Grade.objects.filter(ta=self).aggregate(total=models.Sum('stu-to-ta-rate'))['total']
        self.score = total_score
        return total_score if total_score is not None else 0

    def __str__(self):
        
        try:
            return f"TA: {self.member.first_name} {self.member.last_name}, ID: {self.computed_id}, Score: {self.score}"
        except RecursionError:
            return "TA: Recursion Error"


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    unit = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.unit} units)"



class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    class_addr = models.CharField(max_length=10)
    department_name = models.CharField(max_length=100, default='Science Department')
    semester = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    year_semester = models.CharField(max_length=20, editable=False)

    class Meta:
        unique_together = (('course', 'professor', 'year_semester'),)

    def save(self, *args, **kwargs):
        self.year_semester = f"{self.year}{self.semester}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.title} - Class {self.class_addr}, {self.semester}"



class GroupActivities(models.Model):
    
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('group', 'date'),)

    def __str__(self):
        return f"{self.title} - Group {self.group}"




class Assistance(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ta_feedback = models.TextField(blank=True, null=True)
    is_head_ta = models.BooleanField(default=False)
    semester = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    year_semester = models.CharField(max_length=20, editable=False)

    class Meta:
        unique_together = (('ta', 'group', 'year_semester'),)

    def save(self, *args, **kwargs):
        self.year_semester = f"{self.year}{self.semester}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Assistance by {self.ta.member.first_name} for Group {self.group.id}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    prof_grade = models.IntegerField()
    ta_grade = models.IntegerField()
    semester = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    year_semester = models.CharField(max_length=20, editable=False)
    stu_to_ta_rate = models.IntegerField()

    class Meta:
        unique_together = (('student', 'group', 'ta', 'year_semester'),)

    def save(self, *args, **kwargs):
        self.year_semester = f"{self.year}{self.semester}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Grade for {self.student.member.first_name} in Group {self.group.id}"


class InviteRequest(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ta_request_accepted = models.BooleanField(default=False)
    prof_invite_accepted = models.BooleanField(default=False)
    semester = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    year_semester = models.CharField(max_length=20, editable=False)

    class Meta:
        unique_together = (('group', 'ta', 'year_semester'),)

    def save(self, *args, **kwargs):
        self.year_semester = f"{self.year}{self.semester}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invite Request for TA {self.ta.member.first_name} in Group {self.group.id}"
