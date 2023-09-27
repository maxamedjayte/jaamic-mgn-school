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
    classRaqam=models.CharField(max_length=255,default='')
    studentsCount=models.IntegerField(null=True,blank=True,default=1)
    status=models.BooleanField(default=True)
    academicYear=models.ForeignKey(AcademicYear,on_delete=models.CASCADE,null=True,blank=True)
    dateModified=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name )+' -- '+str(self.classRaqam)


class Students(models.Model):
    fullName=models.CharField(max_length=255)
    gender=models.CharField(default='ذكر',max_length=10)
    image=models.ImageField(upload_to='images/students')
    parentName=models.CharField(max_length=255,default='')
    parentNum=models.CharField(max_length=14,default='')
    dateOfBirth=models.DateField()
    registredDate=models.DateField()
    studentClasse=models.ForeignKey(Classe,on_delete=models.CASCADE,null=True,blank=True)

    