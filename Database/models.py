from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.utils import timezone

class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^(09|\+989)\d{9}$', message="Phone number must be in the format '09xxxxxxxx' or '+989xxxxxxxx'.")
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    linkedIn_addr = models.URLField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    major = models.CharField(max_length=100)
    entry_year = models.PositiveIntegerField()
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Student: {self.member.first_name} {self.member.last_name}, Major: {self.major}, GPA: {self.gpa}"

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Professor(models.Model):
    prof_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    dept = models.ForeignKey('Department', on_delete=models.CASCADE)
    rank = models.CharField(max_length=50)
    study_field = models.CharField(max_length=100)

    def __str__(self):
        return f"Professor: {self.member.first_name} {self.member.last_name}, Rank: {self.rank}, Department: {self.dept.name}"

class TA(models.Model):
    TA_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)

    def __str__(self):
        return f"TA: {self.member.first_name} {self.member.last_name}"

    # @property
    # def score(self):
    #     # Assuming there is a Rating model where ratings are stored
    #     # Example: Rating model has fields 'ta' (ForeignKey to TA), 'score' (Integer)
    #     total_score = Rating.objects.filter(ta=self).aggregate(total=models.Sum('score'))['total']
    #     return total_score if total_score is not None else 0

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.IntegerField()
    activity = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.unit} units)"
    
class Group(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    class_number = models.CharField(max_length=10)
    semester = models.CharField(max_length=10)
    prof_grade = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    TA_grade = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ((student, course, professor),)

    def __str__(self):
        return f"{self.course.name} - Class {self.class_number}, {self.semester}"

class Assistance(models.Model):
    TA = models.ForeignKey(TA, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    TA_feedback = models.TextField(blank=True, null=True)
    is_head_TA = models.BooleanField(default=False)

    class Meta:
        unique_together = ((TA, Group),)

    def __str__(self):
        return f"Assistance by {self.TA.member.first_name} for Group {self.group.id}"
