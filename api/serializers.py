from rest_framework import serializers
from .models import AcademicYear,Subject,Classe,Students,ExamEntring,ExamMarks,Teachers,StudentNotes,TeacherNotes

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



class ExamEntringCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamEntring
        fields = '__all__'


class ExamEntringSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamEntring
        fields = '__all__'
        depth = 3

class ExamMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamMarks
        fields = '__all__'
        depth=3
        

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'
        depth=3

class StudentNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentNotes
        fields = '__all__'
        depth=3

class TeacherNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherNotes
        fields = '__all__'
        depth=3