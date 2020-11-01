from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework import generics
from questionPapers.models import QuestionPaper, Subject
from profiles.models import StudentDetail
from rest_framework.response import Response
from . import serializers
from . import models


# Create your views here.

class upload_question_paper_view(generics.CreateAPIView):
    queryset = models.QuestionPaper.objects.all()
    serializer_class = serializers.QuestionUploadSerializer


class view_subjects(generics.ListAPIView):

    def get(self, request):
        student_id = self.request.user.studentdetail
        student_dept = student_id.branch
        student_year = student_id.year
        subjects_view = Subject.objects.filter(deptName=student_dept).filter(yearNum=student_year)
        return Response(subjects_view.data)


        # student_dept = StudentDetail.objects.get(branch=self.request.branch)
        # student_year = StudentDetail.objects.get(year=self.year)


# class view_question_paper(APIView):

#     def get(self, request):