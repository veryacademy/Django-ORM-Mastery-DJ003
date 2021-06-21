# Django Aggregation
Retrieve values that are derived by summarizing or aggregating a collection of objects. Here we focus on a single table using aggregation

* returns a dictionary of name-value pairs
* Aggregate calculates values for the entire queryset 
* Annotate calculates summary values for each item in the queryset

### Code Examples
---

```python
### ex1.0.1
from book.models import Book
Book.objects.count()
```
```python
### ex1.0.2
from django.db.models import Sum
from book.models import Book
Book.objects.all().aggregate(Sum('ratings_count'))
```

```python
### ex1.0.2
from django.db.models import Max
Book.objects.all().aggregate(Max('average_rating'))
```

```python
### ex1.0.3
from django.db.models import Min
Book.objects.all().aggregate(Min('average_rating'))
```

```python
### ex1.0.4
from django.db.models import Avg
Book.objects.all().aggregate(Avg('average_rating'))

avg = Book.objects.all().aggregate(Avg('average_rating'))
round(avg["average_rating__avg"],0)

# Template - Round numbers
# {{ total|floatformat:1 }}

```
```python
### ex1.0.5
# Difference between the highest average rating book and the average rating of all books.
from django.db.models import FloatField, Avg, Max
Book.objects.aggregate(rating_diff=Max('average_rating', output_field=FloatField()) - Avg('average_rating'))
```

```python
### ex1.0.6
from django.db.models import Avg, Max, Min
Book.objects.filter(authors="John McPhee").aggregate(Avg('average_rating'), Min('average_rating'), Max('average_rating'))
```