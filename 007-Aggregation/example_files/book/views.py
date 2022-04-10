from django.db.models import Sum, Max, Min, Avg
from book.models import Book
from django.shortcuts import render
from django.views.generic import ListView

# def example(request):
#   data = Book.objects.aggregate(sum=Sum('ratings_count'), max=Max('ratings_count'),min=Min('ratings_count'),avg=Avg('ratings_count'))
#   return render(request, 'index.html', {"data":data})


class Example(ListView):
    
    model = Book
    template_name = "index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(Example, self).get_context_data(*args, **kwargs)
        context['ratings_count'] = Book.objects.aggregate(Sum('ratings_count'))
        return context    