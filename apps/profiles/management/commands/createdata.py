from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from faker import Faker
from django.contrib.auth.models import User
import sys
import os
sys.path.append(os.path.join(os.path.dirname("createdata.py"), '../../..'))
from profiles.models import StudentDetail, FacultyDetail
from questionPapers.models import Course, Branch, Year, Subject


class Command(BaseCommand):
    help = 'Create random model instances and groups for testing purposes.'

    def add_arguments(self, parser):
        pass
        parser.add_argument('--dummydata', action='store_true', help='Create dummy data')
        parser.add_argument('--coursedata', action='store_true', help='Create dummy course data')

    def handle(self, *attrs, **options):

        _, created = Group.objects.get_or_create(name='student')
        _, created = Group.objects.get_or_create(name='faculty')
        _, created = Group.objects.get_or_create(name='management')
        _, created = Group.objects.get_or_create(name='hod')
        _, created = Group.objects.get_or_create(name='others')

        if options['dummydata']:
            fake = Faker()

            # Create admin
            User.objects.create_superuser(username='admin123', email='', password='adminadmin')

            # Create 5 users of each group respectively
            groups = ['student', 'faculty', 'management', 'hod', 'others']

            for group_name in groups:
                for i in range(0, 5):
                    name = fake.name()
                    first_name = name.split(' ')[0]
                    last_name = ' '.join(name.split(' ')[-1:])
                    username = first_name[0].lower() + last_name.lower().replace(' ', '')
                    user = User.objects.create_user(username, password=username)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.is_superuser = False
                    user.email = username + "@" + last_name.lower() + ".com"
                    users_group = Group.objects.get(name=group_name)
                    users_group.user_set.add(user)
                    user.save()
                    user.save()
                    if (str(group_name) == "student"):
                        StudentDetail.objects.create(user=user)
                    else:
                        FacultyDetail.objects.create(user=user)

        if options['coursedata']:

            # Create Course Instances
            courses = {'BTech': 'Bachelor of Technology',
                       'MTech': 'Master of Engineering',
                       'MBA': 'Master of Business Administration'}

            for courseCode, courseName in courses.items():
                Course.objects.create(courseCode=courseCode, courseFullName=courseName)

            # Creates Branch Instances
            branchesBTech = {'CSE': 'Computer Science and Engineering',
                             'ECE': 'Electrical & Computer Engineering'}

            branchesMTech = {'PE': 'Production Engineering'}

            branchesMBA = {'KMBHR': 'Human Resource',
                           'KMBIB': 'International Business'}

            for branchCode, branchName in branchesBTech.items():
                Branch.objects.create(course=Course.objects.get(courseCode='BTech'), deptCode=branchCode, deptFullName=branchName)

            for branchCode, branchName in branchesMTech.items():
                Branch.objects.create(course=Course.objects.get(courseCode='MTech'), deptCode=branchCode, deptFullName=branchName)

            for branchCode, branchName in branchesMBA.items():
                Branch.objects.create(course=Course.objects.get(courseCode='MBA'), deptCode=branchCode, deptFullName=branchName)

            # Create Years
            for year in range(1, 5):
                Year.objects.create(number=year)

            # Create Subjects
            subjects = [['CSE', 'KCS403', 'Microprocessor', 2],
                        ['CSE', 'KCS601', 'Software Engineering', 3],
                        ['ECE', 'KEC501', 'Integrated Circuits', 3],
                        ['ECE', 'REC702', 'VLSI Design', 4],
                        ['PE', 'MTME101', 'Simulation, Modelling & Analysis', 1],
                        ['KMBHR', 'KMB301', 'Strategic Management', 1],
                        ['KMBIB', 'KMBIB04', 'International Trade Laws', 2]]

            for subject in subjects:
                Subject.objects.create(deptName=Branch.objects.get(deptCode=subject[0]),
                                       yearNum=Year.objects.get(number=subject[3]),
                                       subCode=subject[1],
                                       subName=subject[2])
