
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('student-teacher/<str:operation>',views.student_teacher,name="student-teacher"),
    path('verify-certificate/<str:token>',views.verify_certificate,name="verify-certificate"),
    
]