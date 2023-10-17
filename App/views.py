from django.shortcuts import render, redirect
from .models import Teacher,Student
from .utils import render_to_pdf
from datetime import datetime,date

def index(request):
    return render(request,"index.html",{})


def student_teacher(request,operation):
    allteachers= Teacher.objects.all()
    allstudents= Student.objects.all()

    if operation=="get-data":
        teacher_id = request.POST.get('teacher')
        student_id = request.POST.get('student')

        if teacher_id!="None":
            teacher = Teacher.objects.get(pk=teacher_id)
            students_4_teacher= teacher.students.all()

            return render(request,"studentteacher.html",{"allstudents":allstudents,"allteachers":allteachers,"students_4_teacher":students_4_teacher})
        
        if student_id!="None":
            student = Student.objects.get(pk=student_id)
            teachers_4_student = student.teacher_set.all()

            return render(request,"studentteacher.html",{"allstudents":allstudents,"allteachers":allteachers,"teachers_4_student":teachers_4_student})

        return redirect("/student-teacher/default")

    elif operation=="generate-certificate":
        teacher_id = request.POST.get("teacher")
        student_id = request.POST.get("student")

        if teacher_id=="None":
            return redirect("/student-teacher/default")
        if student_id=="None":
            return redirect("/student-teacher/default")
        
        teacher = Teacher.objects.get(id=teacher_id)
        student = Student.objects.get(id=student_id)

        template_name = "certificate-template.html"

        return render_to_pdf(template_name,{"teacher":teacher.name,
                "student":student.name,
                "date":date.today(),
            },
    )
    
    else:
        return render(request,"studentteacher.html",{"allstudents":allstudents,"allteachers":allteachers})
    


def students_for_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    students = teacher.students.all()
    return render(request, 'students_for_teacher.html', {'teacher': teacher, 'students': students})

def teachers_for_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    teachers = student.teacher_set.all()
    return render(request, 'teachers_for_student.html', {'student': student, 'teachers': teachers})