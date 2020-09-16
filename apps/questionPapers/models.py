from django.db import models
from profiles.models import FacultyDetail
from django.core.validators import RegexValidator
# Create your models here.


class Semester(models.Model):
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.number)


class Subject(models.Model):
    semNum = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class QuestionPaper(models.Model):

    uploadedBy = models.ForeignKey(FacultyDetail, null=False, on_delete=models.CASCADE)
    questionPaperFile = models.FileField(upload_to="attachments", null=False)
    forSubject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ofYear_regex = RegexValidator(
        regex=r'^\d{4}[-]\d{4}',
        message="Ex - 2020-2021")
    ofYear = models.CharField(validators=[ofYear_regex], max_length=9)
