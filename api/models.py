from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.


class UserProfile(AbstractUser):
    profileImage=models.ImageField(upload_to='images/profiles',null=True,blank=True)
    groups = models.ManyToManyField(Group, related_name='user_profile_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_profile_permessions')





class AcademicYear(models.Model):
    fromDate=models.CharField(max_length=255,default='2022')
    toDate=models.CharField(max_length=255,default='20223')
    isCurrentAcademicYear=models.BooleanField(default=False)
    desc=models.TextField(null=True,blank=True)
    dateModified=models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        AcademicYear.objects.exclude(id=self.id).update(isCurrentAcademicYear=False)

        super(AcademicYear, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-isCurrentAcademicYear']

    def __str__(self) -> str:
        return str(self.fromDate)+' -- '+str(self.toDate)

class Subject(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField(null=True,blank=True)
    dateModified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

class Classe(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    subjects=models.ManyToManyField(Subject,blank=True)
    classRaqam=models.CharField(max_length=255,default='',null=True,blank=True)
    studentsCount=models.IntegerField(null=True,blank=True,default=1)
    status=models.BooleanField(default=True)
    academicYear=models.ForeignKey(AcademicYear,on_delete=models.CASCADE,null=True,blank=True)
    dateModified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name )+' -- '+str(self.classRaqam)


class Students(models.Model):
    fullName=models.CharField(max_length=255)
    gender=models.CharField(default='ذكر',max_length=10)
    image=models.ImageField(upload_to='images/students',null=True,blank=True)
    parentName=models.CharField(max_length=255,default='')
    parentNum=models.CharField(max_length=14,default='')
    dateOfBirth=models.DateField(null=True,blank=True)
    registredDate=models.DateField(null=True,blank=True)
    studentClasse=models.ForeignKey(Classe,on_delete=models.CASCADE,null=True,blank=True)
    motherName=models.CharField(max_length=255,default='')
    placeOfBirth=models.CharField(max_length=255,null=True,blank=True)
    living=models.CharField(max_length=255,null=True,blank=True)

    

    def __str__(self) -> str:
        return str(self.fullName)
    

class ExamEntring(models.Model):
    examName=models.CharField(max_length=255)
    examDate=models.DateField(null=True,blank=True)
    academicYear=models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    classe=models.ManyToManyField(Classe,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.examName)+' -- '+str(self.examDate)
    
class ExamMarks(models.Model):
    student=models.ForeignKey(Students,on_delete=models.CASCADE)
    exam=models.ForeignKey(ExamEntring,on_delete=models.CASCADE)
    classe=models.ForeignKey(Classe,on_delete=models.CASCADE,null=True,blank=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    mark=models.IntegerField(null=True,blank=True)
    dateModified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.student)+' -- '+str(self.exam)+' -- '+str(self.subject)+' -- '+str(self.mark)
    


class Teachers(models.Model):
    name=models.CharField(max_length=255)
    gender=models.CharField(default='ذكر',max_length=10)
    salary=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to='images/teachers',null=True,blank=True)
    phone=models.CharField(max_length=14,null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    status=models.BooleanField(default=True)
    dateRegistred=models.DateField(null=True,blank=True)
    educatingClasses=models.ManyToManyField(Classe,null=True,blank=True)
    educatingSubjects=models.ManyToManyField(Subject,null=True,blank=True)
    educationLevel=models.CharField(max_length=255,null=True,blank=True)


    def __str__(self) -> str:
        return str(self.name) + ' -- '+str(self.title)