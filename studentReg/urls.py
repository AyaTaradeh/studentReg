from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('courses/',views.courses),
    path('coursesScheduls/',views.coursesScheduls),
    path('students/',views.students),
    path('studentsReg/',views.studentsReg),
]