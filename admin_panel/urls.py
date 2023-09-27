from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard),
    path('login/',views.loginUser),
    path('logout/',views.logoutUser),
    
    path('academic-year/',views.academicYear),


    # manage-classes
    path('register-classes/',views.registerClasses),
    path('manage-classes/',views.manageClasses),
    path('classe-detail/<str:pk>/<str:name>/',views.classeDetail),


    # manage-subjects
    path('manage-subject/',views.manageSubjects),

    # manage-subjects
    path('register-student/',views.registerStudent),
    path('manage-student/',views.manageStudent),
    path('student-detail/<str:pk>/<str:name>/',views.studentDetail),


    path('search-student/',views.academicYear),

]