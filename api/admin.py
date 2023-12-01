from django.contrib import admin
from .models import UserProfile,Students,Classe,ExamEntring,ExamMarks,AcademicYear
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(AcademicYear)
admin.site.register(Students)
admin.site.register(Classe)
admin.site.register(ExamEntring)
admin.site.register(ExamMarks)