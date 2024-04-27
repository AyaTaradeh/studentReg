from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"register/index.html")
def courses(request):
    return render(request,"register/courses.html")
def coursesScheduls(request):
    return render(request,"register/coursesScheduls.html")
def students(request):
    return render(request,"register/students.html")
def studentsReg(request):
    return render(request,"register/studentsReg.html")