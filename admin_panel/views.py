from django.shortcuts import render,redirect
from api.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    subjects=Subject.objects.all()
    classes=Classe.objects.all()
    students=Students.objects.all()
    latest_students=students.order_by('-registredDate')[:5].all()

    return render(request,'normal-pages/dashboard.html',{'subjects':subjects,'students':students,'classes':classes,'latest_students':latest_students})


@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    
    return redirect("/login/")

def loginUser(request):
    status=''
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            status='Usernameka ama Passwordka ayaa qaldan'
    data={
        'status':status
    }
    return render(request,'normal-pages/login.html',data)


@login_required(login_url='/login/')
def academicYear(request):
    return render(request,'reg-manage/academic-year.html')



@login_required(login_url='/login/')
def manageSubjects(request):
    return render(request,'reg-manage/subjects.html')




@login_required(login_url='/login/')
def registerClasses(request):
    subjects=Subject.objects.all()
    academicYears=AcademicYear.objects.all()
    return render(request,'reg-manage/register-class.html',{'subjects':subjects,'academicYears':academicYears})


@login_required(login_url='/login/')
def manageClasses(request):
    classes=Classe.objects.all()
    for cls in classes:
        cls.studentsCount=Students.objects.filter(studentClasse=cls.pk).count()
    return render(request,'reg-manage/manage-classes.html',{"classes":classes})

@login_required(login_url='/login/')
def classeDetail(request,pk,name):
    classe=Classe.objects.filter(pk=pk).first()
    classStudents=Students.objects.filter(studentClasse=classe.pk)
    return render(request,'detail-pages/classe-detail.html',{'classeDetail':classe,"classStudents":classStudents})








def registerStudent(request):
    classes=Classe.objects.all()
    return render(request,'reg-manage/register-student.html',{'classes':classes})

def studentDetail(request,pk,name):
    classes=Classe.objects.all()
    student=Students.objects.filter(pk=pk).first()
    return render(request,'detail-pages/student-detail.html',{'studentDetail':student,"classes":classes})

def manageStudent(request):
    students=Students.objects.all()
    return render(request,'reg-manage/manage-student.html',{"students":students})



@login_required(login_url='/login/')
def registerManageExams(request):
    examEntrings=ExamEntring.objects.all()
    classes=Classe.objects.all()
    academicYears=AcademicYear.objects.all()
    return render(request,'reg-manage/register-manage-exams.html',{'examEntrings':examEntrings,'classes':classes,'academicYears':academicYears})



@login_required(login_url='/login/')
def manageExamMarks(request):
    academicYears=AcademicYear.objects.all()
    
    return render(request,'reg-manage/manage-exam-marks.html',{'academicYears':academicYears})