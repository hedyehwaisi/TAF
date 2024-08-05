from django.db import models
from django.core.validators import RegexValidator


class Member(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('ta', 'TA'),
        ('professor', 'Professor'),
    ]

    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    linkedIn_addr = models.URLField(blank=True )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MemberPhone(models.Model):
    Type = [
        ('null', ''),
        ('work', 'Work'),
        ('personal', 'Personal'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^(09|\+989)\d{9}$',
                                 message="Phone number must be in the format '09xxxxxxxxx' or '+989xxxxxxxxx'.")
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True, blank=True)
    phone_type = models.CharField(max_length=255, choices=Type, default='', blank=True)

    def __str__(self):
        return f"{self.phone_type}: {self.phone}"


class MemberEmail(models.Model):
    Type = [
        ('work', 'Work'),
        ('personal', 'Personal'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, blank=True)
    email_type = models.CharField(max_length=255, choices=Type, default='Personal', blank=True)

    def __str__(self):
        return f"{self.email_type}: {self.email}"


class Student(models.Model):
    major = [
        ('cs', 'Computer Science'),
        ('math', 'Mathmatics'),
        ('statis', 'Statistics'),
    ]
    
    member = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    major = models.CharField(max_length=100, choices=major, default='Computer Science')
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
    def score_computing(self):
        total_score = Grade.objects.filter(ta=self).aggregate(total=models.Sum('stu_to_ta_rate'))['total']
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

    deps = {
        ('science', 'Science Department'),
        ('engineering', 'Engineering Department'),

    }

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    class_addr = models.CharField(max_length=10)
    department_name = models.CharField(max_length=100, choices=deps, default='Science Department')
    semester = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    year_semester = models.CharField(max_length=20, editable=False)

    class Meta:
        unique_together = (('course', 'professor', 'year_semester'),)

    def save(self, *args, **kwargs):
        self.year_semester = f"{self.year}{self.semester}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.title} - Class {self.class_addr}, {self.year_semester}"


class Assistance(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ta_feedback = models.TextField(blank=True, null=True)
    is_head_ta = models.BooleanField(default=False)

    class Meta:
        unique_together = (('ta', 'group'),)

    def save(self, *args, **kwargs):
        self.year_semester = f"{self.group.year}{self.group.semester}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Assistance by {self.ta.member.first_name} for Group {self.group.id}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # assistance = models.ForeignKey(Assistance, on_delete=models.CASCADE)
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    prof_grade = models.IntegerField()
    ta_grade = models.IntegerField()
    stu_to_ta_rate = models.IntegerField()

    class Meta:
        unique_together = (('student', 'group', 'ta'),)

    def __str__(self):
        return f"Grade for {self.student.member.first_name} in Group {self.group.id}"


class GroupActivities(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('group', 'date'),)

    def __str__(self):
        return f"{self.title} - Group {self.group}"


class InviteRequest(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    prof_to_TA_feedback = models.IntegerField()
    ta_request_accepted = models.BooleanField(default=False)
    prof_invite_accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = (('group', 'ta'),)

    def __str__(self):
        return f"Invite Request for TA {self.ta.member.first_name} in Group {self.group.id}"
