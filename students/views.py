from django.db.models import Q
from django.shortcuts import render

from students.models import Student, Teacher
from django.db import connection


# def student_list(request):
#     post = Student.objects.all()
#     print(post)
#     print(connection.queries)
#     return render(request, 'output.html', {'posts': post})


# def student_list(request):
#     post = Student.objects.filter(Q(last_name__startswith='Aidaraliev') |
#                                   Q(last_name__startswith='last name 2') |
#                                   Q(last_name__startswith='last name'))
#
#     print(post)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': post})


# def student_list(request):
#     post = Student.objects.filter(Q(class_room=4) & Q(first_name__startswith='Adilet'))
#
#     print(post)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': post})


# def student_list(request):
#     post = Student.objects.all().values_list('first_name').union(
#         Teacher.objects.all().values_list('first_name'))
#     print(post)
#     print(connection.queries)
#
#     return render(request, 'output.html', {'posts': post})


# def student_list(request):
#     # post = Student.objects.exclude(age__gt=1)
#     post = Student.objects.filter(teacher__startswith='Talant')
#     print(post)
#     print(connection.queries)
#     return render(request, 'output.html', {'posts': post})


# def student_list(request):
#     post = Student.objects.filter(~Q(age=3) & ~Q(first_name__startswith='first name 1'))
#
#     print(post)
#     print(connection.queries)
#     return render(request, 'output.html', {'posts': post})


# def student_list(request):
#     post = Student.objects.filter(Q(age=1)).only('first_name', 'class_room')
#
#     print(post)
#     print(connection.queries)
#     return render(request, 'output.html', {'posts': post})


def student_list(request):

    sql = "SELECT * FROM students_student WHERE teacher='Arzhycan'"
    post = Student.objects.raw(sql)

    print(post)
    print(connection.queries)
    return render(request, 'output.html', {'posts': post})
