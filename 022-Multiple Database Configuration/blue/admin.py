from django.contrib import admin

from .models import Blue

class BlueAdmin(admin.ModelAdmin):
    using = 'blue'
    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)
    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)
    def delete_model(self, request, obj):
        obj.delete(using=self.using)

admin.site.register(Blue, BlueAdmin)