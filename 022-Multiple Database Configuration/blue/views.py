from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Blue
from aqua.models import Aqua
from django.http import HttpResponseRedirect

def viewdata(request):
    data = Blue.objects.using('blue_db').all()
    return render(request, "view.html", {"data": data})

class Add(CreateView):
  model = Aqua
  fields = ('title','content','app_name' )
  template_name = 'add.html'
  success_url = '/blue/'

  def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())