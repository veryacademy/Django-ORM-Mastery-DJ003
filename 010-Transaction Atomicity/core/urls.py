from django.contrib import admin
from django.urls import path
from bank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.process_payment, name='payment')
]
