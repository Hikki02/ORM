from django.db.models import Q
from django.shortcuts import render

from students.models import Student
from django.db import connection


def student_list_(request):
    post = Student.objects.all()
    print(post)
    print(connection.queries)
    return render(request, 'output.html', {'posts': post})


def student_list(request):
    post = Student.objects.filter(Q(last_name__startswith='Aidaraliev') |
                                  Q(last_name__startswith='last name 2') |
                                  Q(last_name__startswith='last name'))

    print(post)
    print(connection.queries)

    return render(request, 'output.html', {'posts': post})
