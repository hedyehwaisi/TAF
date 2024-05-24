from tables.models import Professor, Course, TA, Student, Enrollment

# Create a professor
prof = Professor.objects.create(first_name='John', last_name='Doe', department='Computer Science')

# Create a course
course = Course.objects.create(title='Intro to Programming', code='CS101', professor=prof, credits=4)

# Create a TA
ta = TA.objects.create(first_name='Jane', last_name='Smith', course=course)

# Create a student
student = Student.objects.create(first_name='Alice', last_name='Johnson')

# Enroll the student in the course
enrollment = Enrollment.objects.create(student=student, course=course, date_enrolled='2023-01-01')
