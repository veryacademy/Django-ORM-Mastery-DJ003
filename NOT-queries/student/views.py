from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################

################
# Simple OR
################

def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})


# Part 3
#################################################################

################
# Simple AND
################

def student_list_(request):
    posts = Student.objects.filter(classroom=1) & Student.objects.filter(age=20)

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='baldwin')&Q(firstname__startswith='lakisha'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

# Part 4
#################################################################

################
# Simple UNION
################

def student_list_(request):

    posts = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))

    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'posts': posts})

# Part 5
#################################################################

################
# Simple EXCLUDE
################

def student_list_(request):

    posts = Student.objects.exclude(age__gt=19)

    # gt
    # gte
    # lt
    # lte

    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'posts': posts})

def student_list(request):

    posts = Student.objects.filter(~Q(age__gt=20)&~Q(surname__startswith='baldwin'))

    print(posts)
    print(connection.queries)
    return render(request,'output.html',{'posts': posts})