from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add_student'),             # → http://localhost:8000/
    path('students/', views.student_list, name='student_list'),  # → http://localhost:8000/students/
]
