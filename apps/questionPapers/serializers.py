from rest_framework import serializers
from questionPapers.models import Subject, QuestionPaper


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['name']


class QuestionUploadSerializer(serializers.ModelSerializer):

    Subject = SubjectSerializer(required=True)
    questionPaperFile = serializers.FileField()

    class Meta:
        model = QuestionPaper
        fields = ['Subject', 'questionPaperFile', 'ofYear']

    def create(self, validated_data):
        sub_data = validated_data.pop('Subject')
        subject = Subject.objects.create(**sub_data)
        pdf_file_data = validated_data.pop('questionPaperFile')
        QuestionPaperInstance = QuestionPaper.objects.create(forSubject=subject, questionPaperFile=pdf_file_data, **validated_data)
        QuestionPaperInstance.save()
        return QuestionPaperInstance
