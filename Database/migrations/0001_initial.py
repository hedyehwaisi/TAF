# Generated by Django 5.0.6 on 2024-06-07 14:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('linkedIn_addr', models.URLField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_addr', models.CharField(max_length=10)),
                ('department_name', models.CharField(default='Science Department', max_length=100)),
                ('semester', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('year_semester', models.CharField(editable=False, max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.course')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Database.member')),
                ('profRank', models.CharField(max_length=50)),
                ('research_field', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Database.member')),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('major', models.CharField(max_length=100)),
                ('entry_year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Database.member')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MemberEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('email_type', models.CharField(max_length=255)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format '09xxxxxxxxx' or '+989xxxxxxxxx'.", regex='^(09|\\+989)\\d{9}$')])),
                ('phone_type', models.CharField(max_length=255)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.member')),
            ],
        ),
        migrations.CreateModel(
            name='GroupActivities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.group')),
            ],
            options={
                'unique_together': {('group', 'date')},
            },
        ),
        migrations.AddField(
            model_name='group',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.professor'),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('course', 'professor', 'year_semester')},
        ),
        migrations.CreateModel(
            name='InviteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_to_TA_feedback', models.IntegerField()),
                ('ta_request_accepted', models.BooleanField(default=False)),
                ('prof_invite_accepted', models.BooleanField(default=False)),
                ('semester', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('year_semester', models.CharField(editable=False, max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.group')),
                ('ta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.ta')),
            ],
            options={
                'unique_together': {('group', 'ta', 'year_semester')},
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_grade', models.IntegerField()),
                ('ta_grade', models.IntegerField()),
                ('stu_to_ta_rate', models.IntegerField()),
                ('semester', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('year_semester', models.CharField(editable=False, max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.group')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.student')),
                ('ta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.ta')),
            ],
            options={
                'unique_together': {('student', 'group', 'ta', 'year_semester')},
            },
        ),
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta_feedback', models.TextField(blank=True, null=True)),
                ('is_head_ta', models.BooleanField(default=False)),
                ('semester', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('year_semester', models.CharField(editable=False, max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.group')),
                ('ta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.ta')),
            ],
            options={
                'unique_together': {('ta', 'group', 'year_semester')},
            },
        ),
    ]
