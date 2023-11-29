from django.contrib import admin
from .models import UserProfile,Students,Classe,ExamEntring
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Students)
admin.site.register(Classe)
admin.site.register(ExamEntring)