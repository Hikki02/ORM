from django.db.models import Q
from django.shortcuts import render

from students.models import Student, Teacher
from django.db import connection


def student_list_(request):
    post = Student.objects.all()
    print(post)
    print(connection.queries)
    return render(request, 'output.html', {'posts': post})


def student_list__(request):
    post = Student.objects.filter(Q(last_name__startswith='Aidaraliev') |
                                  Q(last_name__startswith='last name 2') |
                                  Q(last_name__startswith='last name'))

    print(post)
    print(connection.queries)

    return render(request, 'output.html', {'posts': post})


def student_list___(request):
    post = Student.objects.filter(Q(class_room=4) & Q(first_name__startswith='Adilet'))

    print(post)
    print(connection.queries)

    return render(request, 'output.html', {'posts': post})


def student_list(request):
    post = Student.objects.all().values_list('first_name').union(
        Teacher.objects.all().values_list('first_name'))
    print(post)
    print(connection.queries)

    return render(request, 'output.html', {'posts': post})

