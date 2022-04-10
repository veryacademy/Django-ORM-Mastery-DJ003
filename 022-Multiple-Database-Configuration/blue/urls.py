from django.urls import path

from . import views

urlpatterns = [
    path('view/', views.viewdata, name='viewdata'),
    path('', views.Add.as_view(), name="addblue"),
]
