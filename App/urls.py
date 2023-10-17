
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('student-teacher/<str:operation>',views.student_teacher,name="student-teacher"),
    
    path('students-for-teacher/<int:teacher_id>/', views.students_for_teacher, name='students-for-teacher'),
    path('teachers-for-student/<int:student_id>/', views.teachers_for_student, name='teachers-for-student'),
]