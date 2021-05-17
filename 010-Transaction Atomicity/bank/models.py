from django.db import models

class customer(models.Model):
  name = models.CharField(max_length=50)
  balance = models.DecimalField(max_digits=5, decimal_places=2)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name