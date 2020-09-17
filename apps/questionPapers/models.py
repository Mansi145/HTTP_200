from django.db import models
from profiles.models import FacultyDetail
from django.core.validators import RegexValidator
# Create your models here.


class Course(models.Model):
    courseCode = models.CharField(max_length=10)
    courseFullName = models.CharField(max_length=30)

    def __str__(self):
        return self.courseCode


class Branch(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    deptCode = models.CharField(max_length=10)
    deptFullName = models.CharField(max_length=100)

    def __str__(self):
        return self.deptCode


class Year(models.Model):

    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.number)


class Subject(models.Model):

    yearNum = models.ForeignKey(Year, on_delete=models.CASCADE)
    deptName = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subName = models.CharField(max_length=30)
    subCode = models.CharField(max_length=10)

    def __str__(self):
        return self.subName


class QuestionPaper(models.Model):

    uploadedBy = models.ForeignKey(FacultyDetail, null=False, on_delete=models.CASCADE)
    questionPaperFile = models.FileField(upload_to="attachments", null=False)
    forSubject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ofYear_regex = RegexValidator(
        regex=r'^\d{4}[-]\d{4}',
        message="Ex - 2020-2021")
    ofYear = models.CharField(validators=[ofYear_regex], max_length=9)
