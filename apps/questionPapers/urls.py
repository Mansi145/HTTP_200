from django.urls import path
from questionPapers import views

urlpatterns = [
    path(
        'upload_questionPaper/',
        views.upload_question_paper_view.as_view(),
        name="QuestionPaperUploadView"),
    path(
        'courses/',
        views.view_subjects.as_view(),
        name="viewStudentSubjects"),
    # path(
    #     'question_papers/',
    #     views.user_login.as_view(),
    #     name="loginView"),
]
