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


# class view_courses(generics.ListAPIView):

#     def get(self, request):
#         student_course = StudentDetail.objects.get(course=self.course)
#         student_branch = StudentDetail.objects.get(branch=self.branch)
#         student_year = StudentDetail.objects.get(year=self.year)
        # subjects_view = Subject.objects.filter(course=student_course).filter(branch=student_branch).filter(year=student_year)
        # return Response(subjects_view.data)


# class view_question_paper(APIView):

#     def get(self, request):