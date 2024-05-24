from django.db import models

class Professor(models.Model):
    prof_id = models.CharField(primary_key = True, unique = True)
    use_id = models.CharField(primary_key = True, unique = True)
    dept_id = models.CharField(primary_key = True, unique = True)
    rank = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Department(models.Model):
    dept_id = models.CharField(primary_key = True, unique = True)
    dept_name = models.CharField(max_length=50)

    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    credits = models.IntegerField()
    
    def __str__(self):
        return self.title

class TA(models.Model):
    TA_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course, through='Enrollment')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    class Meta:
        unique_together = ('student', 'course')

class Assistance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    class Meta:
        unique_together = ('student', 'course')
