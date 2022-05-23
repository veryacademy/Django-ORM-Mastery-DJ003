from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class Teacher(models.Model):
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Student(models.Model):
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.CheckConstraint(check=(Q(age__gte=10) & Q(age__lte=20)), name="age10-20")
        ]

    def clean(self):
        if self.age > 20 or self.age < 10:
            raise ValidationError({'age':_('Age needs to be under 20.')})
    

    def __str__(self):
        return self.firstname