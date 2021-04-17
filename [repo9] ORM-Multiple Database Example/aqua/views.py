from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Aqua


class Add(CreateView):
    model = Aqua
    fields = ('title','content','app_name' )
    template_name = 'add.html'
    success_url = '/aqua/'