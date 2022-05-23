.delete()
Student.objects.get(pk=1).delete()
Student.objects.filter(pk=1).delete()
Student.objects.filter(id__in=[7,8]).delete()
Student.objects.all().delete()
from django.db import connection
from django.db import reset_queries
reset_queries()