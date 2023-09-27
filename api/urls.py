from django.urls import path
from . import views

from .views import *
urlpatterns = [
    path('academic-years/', AcademicYearListCreate.as_view(), name='academic-year-list-create'),
    path('academic-years/<int:pk>/', AcademicYearDetailDelete.as_view(), name='academic-year-detail-delete'),

    path('subjects/', SubjectListCreate.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectDetailDelete.as_view(), name='subject-detail-delete'),

    path('classes/', ClasseListCreateAPI.as_view(), name='classe-list-create'),
    path('classes/<int:pk>/', ClasseRetrieveUpdateDestroyAPI.as_view(), name='classe-retrieve-update-destroy'),

       path('students/', StudentsListCreate.as_view(), name='students-list-create'),
    path('students/<int:pk>/', StudentsRetriveUpdateDestroyApi.as_view(), name='students-retrive-update-destroy'),
]