from django.contrib import admin
from questionPapers.models import Semester, Subject, QuestionPaper

# Register your models here.

admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(QuestionPaper)