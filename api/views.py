
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import Http404

# Create your views here.
class AcademicYearListCreate(APIView):
    def get(self, request, format=None):
        academic_years = AcademicYear.objects.all()
        serializer = AcademicYearSerializer(academic_years, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AcademicYearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AcademicYearDetailDelete(APIView):
    """
    Retrieve, update or delete an academic year instance.
    """
    def get_object(self, pk):
        try:
            return AcademicYear.objects.get(pk=pk)
        except AcademicYear.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        academic_year = self.get_object(pk)
        serializer = AcademicYearSerializer(academic_year)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        academic_year = self.get_object(pk)
        serializer = AcademicYearSerializer(academic_year, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        academic_year = self.get_object(pk)
        serializer = AcademicYearSerializer(academic_year, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        academic_year = self.get_object(pk)
        academic_year.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class SubjectListCreate(APIView):
    def get(self, request, format=None):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubjectDetailDelete(APIView):
    """
    Retrieve, update or delete a subject instance.
    """
    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subject = self.get_object(pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subject = self.get_object(pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        subject = self.get_object(pk)
        serializer = SubjectSerializer(subject, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ClasseListCreateAPI(APIView):
    def get(self, request, format=None):
        classes = Classe.objects.all()
        serializer = ClasseSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClasseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClasseRetrieveUpdateDestroyAPI(APIView):
    def get_object(self, pk):
        try:
            return Classe.objects.get(pk=pk)
        except Classe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        classe = self.get_object(pk)
        serializer = ClasseSerializer(classe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        classe = self.get_object(pk)
        serializer = ClasseSerializer(classe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        classe = self.get_object(pk)
        classe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




class StudentsListCreate(APIView):
    def get(self, request, format=None):
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsRetriveUpdateDestroyApi(APIView):
    """
    Retrieve, update or delete a student instance.
    """
    def get_object(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentsSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentsSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StudentExamDetail(APIView):
    def get(self, request, pk, format=None):
        student = Students.objects.get(pk=pk)
        examEntring = ExamEntring.objects.filter(academicYear=AcademicYear.objects.filter(isCurrentAcademicYear=True).first())
        examEntringSerializer = ExamEntringSerializer(examEntring, many=True)
        examMarks = ExamMarks.objects.filter(student=student).order_by('classe').order_by('exam').order_by('subject')
        examMarksSerializer = ExamMarksSerializer(examMarks, many=True)
        

        return Response({'examEntrings':examEntringSerializer.data,'examMarks':examMarksSerializer.data})



# student notes
class StudentNotesListCreate(APIView):
    def get(self, request, format=None):
        student_notes = StudentNotes.objects.all()
        serializer = StudentNotesSerializer(student_notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentNotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentNotesRetriveUpdateDestroyApi(APIView):
    """
    Retrieve, update or delete a student notes instance.
    """
    def get_object(self, pk):
        try:
            return StudentNotes.objects.get(pk=pk)
        except StudentNotes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student_notes = self.get_object(pk)
        serializer = StudentNotesSerializer(student_notes)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student_notes = self.get_object(pk)
        serializer = StudentNotesSerializer(student_notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        student_notes = self.get_object(pk)
        serializer = StudentNotesSerializer(student_notes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student_notes = self.get_object(pk)
        student_notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NotesForThisStudent(APIView):
    def get(self, request,pk, format=None):
        student_notes = StudentNotes.objects.filter(student=pk)
        serializer = StudentNotesSerializer(student_notes, many=True)
        return Response(serializer.data)


# teachrs
class TeachersListCreate(APIView):
    def get(self, request, format=None):
        teachers = Teachers.objects.all()
        serializer = TeachersSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeachersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeachersRetriveUpdateDestroyApi(APIView):
    """
    Retrieve, update or delete a teacher instance.
    """
    def get_object(self, pk):
        try:
            return Teachers.objects.get(pk=pk)
        except Teachers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeachersSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeachersSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeachersSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# teacher notes
class TeacherNotesListCreate(APIView):
    def get(self, request, format=None):
        teacher_notes = TeacherNotes.objects.all()
        serializer = TeacherNotesSerializer(teacher_notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherNotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherNotesRetriveUpdateDestroyApi(APIView):
    """
    Retrieve, update or delete a teacher notes instance.
    """
    def get_object(self, pk):
        try:
            return TeacherNotes.objects.get(pk=pk)
        except TeacherNotes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teacher_notes = self.get_object(pk)
        serializer = TeacherNotesSerializer(teacher_notes)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        teacher_notes = self.get_object(pk)
        serializer = TeacherNotesSerializer(teacher_notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        teacher_notes = self.get_object(pk)
        serializer = TeacherNotesSerializer(teacher_notes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teacher_notes = self.get_object(pk)
        teacher_notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









# create full api for exam entring and marks
class ExamEntringListCreate(APIView):
    def get(self, request, format=None):
        exam_entrings = ExamEntring.objects.all()
        serializer = ExamEntringSerializer(exam_entrings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamEntringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExamEntringRetriveUpdateDestroyApi(APIView):
    """
    Retrieve, update or delete an exam entring instance.
    """
    def get_object(self, pk):
        try:
            return ExamEntring.objects.get(pk=pk)
        except ExamEntring.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exam_entrings = self.get_object(pk)
        serializer = ExamEntringSerializer(exam_entrings)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exam_entrings = self.get_object(pk)
        serializer = ExamEntringSerializer(exam_entrings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        exam_entrings = self.get_object(pk)
        serializer = ExamEntringSerializer(exam_entrings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        exam_entrings = self.get_object(pk)
        exam_entrings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GetExamEntringByAcademicYear(APIView):
    def get(self, request, pk, format=None):
        exam_entrings = ExamEntring.objects.filter(academicYear=pk)
        serializer = ExamEntringSerializer(exam_entrings, many=True)
        return Response(serializer.data)


class GetClassesByExamEntrings(APIView):
    def get(self, request, pk, format=None):
        exam_entrings = ExamEntring.objects.filter(classe=pk)
        serializer = ExamEntringSerializer(exam_entrings, many=True)
        return Response(serializer.data)


class PrepareExamMarksForThisClassSubjects(APIView):
    def post(self, request, format=None):
        examEntringID = request.data['examEntring']
        classeID = request.data['classe']
        subjectID = request.data['subject']
        
        print('hellow')
        print(examEntringID)

        students = Students.objects.filter(studentClasse=classeID)
        # for student in students:
        #     print('hellow22222')
        #     if ExamMarks.objects.filter(exam=examEntringID).filter(classe=classeID).filter(subject=subjectID).filter(student=student).exists() == False:
        #         print('hellow33333')
        #         examMarks = ExamMarks.objects.create(
        #             student=student,
        #             exam=ExamEntring.objects.get(pk=examEntringID),
        #             classe=Classe.objects.get(pk=classeID),
        #             subject=Subject.objects.get(pk=subjectID),
        #             mark=0)
        #         examMarks.save()
        #     else:
        #         print('else')
                
        # examMarks = ExamMarks.objects.filter(exam=examEntringID).filter(classe=classeID).filter(subject=subjectID)
        # serializer = ExamMarksSerializer(examMarks, many=True)
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)

class StudentSubjectMarksGetCreate(APIView):
    def post(self, request, format=None):
        examEntringID = request.data['examEntring']
        classeID = request.data['classe']
        subjectID = request.data['subject']
        studentID = request.data['student']

        

        if ExamMarks.objects.filter(exam=examEntringID).filter(classe=classeID).filter(subject=subjectID).filter(student=studentID).exists() == False:
            examMarks = ExamMarks.objects.create(
                student=Students.objects.get(pk=studentID),
                exam=ExamEntring.objects.get(pk=examEntringID),
                classe=Classe.objects.get(pk=classeID),
                subject=Subject.objects.get(pk=subjectID),
                mark=0)
            examMarks.save()


        examMarks = ExamMarks.objects.filter(exam=examEntringID).filter(classe=classeID).filter(subject=subjectID).filter(student=studentID)
        serializer = ExamMarksSerializer(examMarks.last(), many=False)

        return Response(serializer.data)

















class ExamMarksListCreate(APIView):
    def get(self, request, format=None):
        exam_marks = ExamMarks.objects.all()
        serializer = ExamMarksSerializer(exam_marks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamMarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExamMarksRetriveUpdateDestroyApi(APIView):
    """
    Retrieve, update or delete an exam marks instance.
    """
    def get_object(self, pk):
        try:
            return ExamMarks.objects.get(pk=pk)
        except ExamMarks.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exam_marks = self.get_object(pk)
        serializer = ExamMarksSerializer(exam_marks)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exam_marks = self.get_object(pk)
        serializer = ExamMarksSerializer(exam_marks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        exam_marks = self.get_object(pk)
        serializer = ExamMarksSerializer(exam_marks, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        exam_marks = self.get_object(pk)
        exam_marks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)