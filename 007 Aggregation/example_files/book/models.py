from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

class Book(models.Model):

  title = models.CharField(_("title"), max_length=255)
  authors = models.CharField(_("authors"), max_length=255)
  average_rating = models.FloatField(_("average rating"))
  isbn = models.CharField(_("isbn"), max_length=150)
  isbn13 = models.CharField(_("isbn 13"), max_length=150)
  language_code = models.CharField(_("language code"), max_length=10)
  num_pages = models.IntegerField(_("number of pages"))
  ratings_count = models.BigIntegerField(_("rating count"))
  text_review_count = models.BigIntegerField(_("text review count"))
  publication_date = models.DateField(_("publication date"))
  publisher = models.CharField(_("publisher"), max_length=150)

