from django.shortcuts import render, redirect
from .models import Teacher,Student


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
        teacher_id = request.POST["teacher"]
        student_id = request.POST["student"]

        if teacher_id=="None":
            return redirect("/student-teacher/default")
        if student_id=="None":
            return redirect("/student-teacher/default")

        teacher = Teacher.objects.get(pk=teacher_id)
        students_4_teacher= teacher.students.all()

        student = Student.objects.get(pk=student_id)
        teachers_4_student = student.teacher_set.all()

        template_name = "certificate-template.html"

        return render_to_pdf(template_name,{"user":user,
                "rep_order":rep_order,
                "order_id":order_id,
            },
    )
    
    else:
        return render(request,"studentteacher.html",{"allstudents":allstudents,"allteachers":allteachers})
    
    return render(request,"studentteacher.html",{"allstudents":allstudents,"allteachers":allteachers})


def students_for_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    students = teacher.students.all()
    return render(request, 'students_for_teacher.html', {'teacher': teacher, 'students': students})

def teachers_for_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    teachers = student.teacher_set.all()
    return render(request, 'teachers_for_student.html', {'student': student, 'teachers': teachers})