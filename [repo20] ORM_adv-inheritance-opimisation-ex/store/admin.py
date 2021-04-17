from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import Product, Book, Cupboard

class ModelAChildAdmin(PolymorphicChildModelAdmin):

    base_model = Product

@admin.register(Book)
class ProductAdmin(ModelAChildAdmin):
    base_model = Book  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site

@admin.register(Cupboard)
class ProductAdmin(ModelAChildAdmin):
    base_model = Cupboard  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site


@admin.register(Product)
class ProductAdmin(PolymorphicParentModelAdmin):
    base_model = Product  # Optional, explicitly set here.
    child_models = (Book, Cupboard)

