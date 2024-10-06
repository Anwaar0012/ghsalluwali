from django.shortcuts import render
from .models import Employee,Student

# Create your views here.
def index(request):
    return render(request, 'index.html')

def teachers(request):
    employees = Employee.objects.all()
    return render(request, 'shoolapp/teachers/teachers.html', {'employees': employees})
def students(request):
    students = Student.objects.all()
    return render(request, 'shoolapp/students/students.html', {'students': students})
