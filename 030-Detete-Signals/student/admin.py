from django import forms
from django.contrib import admin
from . import models
from . import forms

class StudentAdmin(admin.ModelAdmin):
    form = forms.StudentForm

admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Teacher)