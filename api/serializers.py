from rest_framework import serializers
from .models import AcademicYear,Subject,Classe,Students,ExamEntring,ExamMarks

class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

# create seriazer for exam entring and exam marks
class ExamEntringSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamEntring
        fields = '__all__'

class ExamMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamMarks
        fields = '__all__'
        