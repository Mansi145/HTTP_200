from django.contrib import admin
from questionPapers.models import Course, Branch, Year, QuestionPaper, Subject

# Register your models here.

admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(Year)
admin.site.register(QuestionPaper)
