from django.shortcuts import render, redirect, HttpResponse
from .models import Teacher,Student,Certificate
from .utils import render_to_pdf
from datetime import datetime,date

def index(request):
    return redirect("/student-teacher/default")


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

        try:
            certificate= Certificate.objects.get(teacher=teacher,student=student)
        except:
            new_certificate= Certificate(teacher=teacher, student=student)
            new_certificate.save()


        # Generate JWT Token
        import datetime
        def generateToken(teacher,student):
            payload = {
                "teacher_id": teacher.id,
                "student_id": student.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30) # Token valid for 30 days
            }
            secret_key = "mithun" 
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            return token

        return render_to_pdf("certificate-template.html",{"teacher":teacher.name,
                "student":student.name,
                "date":date.today(),
                "Token":generateToken(teacher,student),
            },
    )
    
    else:
        return render(request,"studentteacher.html",{"allstudents":allstudents,"allteachers":allteachers})
    

import jwt

def verify_certificate(request, token):
    try:
        payload = jwt.decode(token, 'mithun', algorithms=['HS256'])
        print("Pas", payload)
        teacher_id = payload.get('teacher_id')
        student_id = payload.get('student_id')
        certificate = Certificate.objects.get(teacher__id=teacher_id, student__id=student_id)
        
        return render_to_pdf("certificate-template.html",{"teacher":certificate.teacher.name,
                "student":certificate.student.name,
                "date":date.today(),
                "Token":token,
            },)
    
    except jwt.ExpiredSignatureError:
        return HttpResponse('Certificate token has expired.', status=400)
    except jwt.DecodeError:
        print("stue id",student_id)
        print("teachet id",teacher_id)
        return HttpResponse('Certificate token is invalid.', status=400)
    except Certificate.DoesNotExist:
        return HttpResponse('Certificate not found.', status=404)