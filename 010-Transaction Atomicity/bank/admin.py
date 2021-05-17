from django.contrib import admin

from .models import customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')
admin.site.register(customer, CustomerAdmin)