from django.db import models


# Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# Teacher Model
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name