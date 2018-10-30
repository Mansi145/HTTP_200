from notices.models import Notice
from django import forms
from ckeditor.widgets import CKEditorWidget


class NoticeCreateForm(forms.ModelForm):
    CSE = 'CSE'
    IT = 'IT'
    EE = 'EE'
    ECE = 'ECE'
    EEE = 'EEE'
    CE = 'CE'
    IC = 'IC'
    ME = 'ME'
    MT = 'MT'
    MCA = 'MCA'
    MBA = 'MBA'
    MTECH = 'MTECH'
    ALL = 'ALL'
    COURSES = (
        (MCA, 'MCA'),
        (MBA, 'MBA'),
        (MTECH, 'MTECH'),
        (ALL, 'ALL')
    )

    BRANCHES = (
        (CSE, 'CSE'),
        (IT, 'IT'),
        (EE, 'EE'),
        (ECE, 'ECE'),
        (EEE, 'EEE'),
        (CE, 'CE'),
        (IC, 'IC'),
        (ME, 'ME'),
        (MT, 'MT'),
        (ALL, 'ALL')
    )

    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    SEMESTERS = (
        (FIRST, '1'),
        (SECOND, '2'),
        (THIRD, '3'),
        (FOURTH, '4'),
        (FIFTH, '5'),
        (SIXTH, '6'),
        (SEVENTH, '7'),
        (EIGHTH, '8'),
        (ALL, 'ALL')
    )

    class Meta:
        model = Notice
        exclude = ('faculty', 'course_branch_year')
        widgets = {'description': CKEditorWidget, }
